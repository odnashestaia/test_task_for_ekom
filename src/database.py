from pymongo import MongoClient

MONGO_URL = "mongodb://mongo:27017"  # URL MongoDB из Docker Compose
DATABASE_NAME = "forms_db"

# Инициализация MongoDB клиента
client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]  # Имя базы
templates_collection = db["templates"]  # Коллекция шаблонов