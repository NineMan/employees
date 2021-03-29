import json
from pymongo import MongoClient


filename = "mongo-seed/employees.json"
# filename = "mongo-seed/employees_short.json"


with open(filename, "r") as f:
    data = json.load(f)

client = MongoClient("localhost", 27017)
db = client.employees
employees_collection = db.employees_collection
employees_id = employees_collection.insert_many(data).inserted_ids
print("Вставлено {} записей в коллекцию".format(len(employees_id)))
