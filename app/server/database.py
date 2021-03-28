from bson.objectid import ObjectId
import motor.motor_asyncio


MONGO_DETAIL = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAIL)

database_e = client.employees

employees_collection = database_e.get_collection("employees_collection")


# helpers
def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "age": employee["age"],
        "company": employee["company"],
        "join_date": employee["join_date"],
        "job_title": employee["job_title"],
        "gender": employee["gender"],
        "salary": employee["salary"],
    }


# Получить список всех сотрудников
async def retrieve_all_employees() -> list:
    employees = []
    async for employee in employees_collection.find():
        employees.append(employee_helper(employee))
    return employees


# Добавить нового сотрудника в базу данных
async def add_employee(employee_data: dict) -> dict:
    employee = await employees_collection.insert_one(employee_data)
    new_employee = await employees_collection.find_one({"_id": employee.inserted_id})
    return employee_helper(new_employee)


# Получить данные сотрудника по ID
async def retrieve_employee(id: str) -> dict:
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)


# Обновить данные сотрудника по ID
async def update_employee(id: str, data: dict) -> bool:
    # Возвращаем ошибку, если был послан пустой запрос
    if len(data) < 1:
        return False
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    print(employee)
    if employee:
        updated_employee = await employees_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        if updated_employee:
            return True
        return False


# Удалить сотрудника из БД
async def delete_employee(id: str) -> bool:
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        await employees_collection.delete_one({"_id": ObjectId(id)})
        return True


# Получить список сотрудников с фильтрацией по полю "gender"
async def retrieve_employees_by_gender(gender: str) -> list:
    employees = []

    async for employee in employees_collection.find({"gender": gender}):
        employees.append(employee_helper(employee))
    return employees


# Получить список сотрудников с фильтрацией по компании
async def retrieve_employees_by_company(company: str) -> list:
    employees = []

    async for employee in employees_collection.find({"company": company}):
        employees.append(employee_helper(employee))
    return employees


# Получить список сотрудников с фильтрацией по возрасту
async def retrieve_employees_by_age(age: int) -> list:
    employees = []

    async for employee in employees_collection.find({"age": age}):
        employees.append(employee_helper(employee))
    return employees


async def retrieve_employees_by_salary(salary: int, direction: bool) -> list:
    """
    Получение сотрудников с фильтрацией по зарплате
    Для фильтрации больше чем: direction=True
    Для фильтрации меньше чем: direction=False
    """

    employees = []

    if direction:
        async for employee in employees_collection.find({"salary": {"$gte": salary}}):
            employees.append(employee_helper(employee))
    else:
        async for employee in employees_collection.find({"salary": {"$lte": salary}}):
            employees.append(employee_helper(employee))

    return employees
