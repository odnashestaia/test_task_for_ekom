from pymongo import MongoClient

MONGO_URL = "mongodb://mongo:27017"  # URL MongoDB из Docker Compose
DATABASE_NAME = "forms_db"

# Инициализация MongoDB клиента
client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]  # Имя базы
templates_collection = db["templates"]  # Коллекция шаблонов

templates = [
    {
        "name": "Contact Form",
        "f_name1": "email",
        "f_name2": "phone",
    },
    {
        "name": "Feedback Form",
        "f_name1": "text",
        "f_name2": "text",
    },
    {
        "name": "Registration Form",
        "f_name1": "date",
        "f_name2": "phone",
    }
]
templates_collection.delete_many({})
result = templates_collection.insert_many(templates)

print("Sucsses inserted templates")
