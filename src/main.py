from fastapi import FastAPI
from .database import templates_collection
from .validators import determine_field_type

app = FastAPI()

@app.post("/get_form")
def get_form(form_data: dict):
    """
    Проверяем данные из формы и ищем соответствующий шаблон
    """
    # Определяем типы данных по каждому значению в форме
    typed_fields = {
        key: determine_field_type(value) for key, value in form_data.items() if key not in ['name']
    }

    # Проверяем, что имя формы есть в запросе
    form_name = form_data.get("name")
    if not form_name:
        return typed_fields

    # Получаем все шаблоны из БД
    templates = list(templates_collection.find())

    # Проверяем каждое определение шаблона
    for template in templates:
        # Проверяем соответствие имени формы
        if template.get("name") != form_name:
            continue

        # Преобразуем шаблон в формат для сравнения
        template_fields = {
            key: template[key] for key in template if key not in ['_id', 'name']
        }
        # Сравниваем все поля по типу
        if all(
            key in typed_fields and typed_fields[key] == field_type
            for key, field_type in template_fields.items()
        ):
            return {"template_name": template["name"]}

    # Если совпадений не найдено
    return typed_fields