import json, sys
from pymongo import MongoClient


# ToDo: вставить имя файла, бд, коллекции и соединения с БД из окружения
filename = "employees.json"
# db_name = "?"
# db_collection = "?"


with open(filename, "r") as f:
    data = json.load(f)

client = MongoClient()
db = client.employees
employees_collection = db.employees_collection
employees_id = employees_collection.insert_many(data).inserted_ids
print("Вставлено {} записей в коллекцию".format(len(employees_id)))

# for id in employees_id:
#     print(id)
