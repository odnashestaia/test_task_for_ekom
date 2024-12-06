import re
from datetime import datetime


def determine_field_type(value: str) -> str:
    """
    Определяем тип данных: email, телефон, дата или текст
    """

    # Проверка на дату
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for fmt in date_formats:
        try:
            datetime.strptime(value, fmt)
            return "date"
        except ValueError:
            continue

    # Проверка на телефон
    phone_pattern = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"
    if re.match(phone_pattern, value):
        return "phone"

    # Проверка на email
    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
    if re.match(email_pattern, value):
        return "email"

    # По умолчанию текст
    return "text"
