from bson.objectid import ObjectId
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb", 27017)

database = client.employees

employees_collection = database.get_collection("employees_collection")


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


async def retrieve_all_employees() -> list:
    """Получение списка всех сотрудников в БД"""

    employees = []
    async for employee in employees_collection.find():
        employees.append(employee_helper(employee))
    return employees


async def add_employee(employee_data: dict) -> dict:
    """
    Добавление нового сотрудника в коллекцию

    :param employee_data:
    :return:
    """

    employee = await employees_collection.insert_one(employee_data)
    new_employee = await employees_collection.find_one(
        {"_id": employee.inserted_id}
    )
    return employee_helper(new_employee)


async def retrieve_employee(id: str) -> dict:
    """
    Получение полных данных сотрудника по ID

    :param id:
    :return:
    """

    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)


async def update_employee(id: str, data: dict) -> bool:
    """
    Обновление данных сотрудника по ID

    :param id:
    :param data:
    :return:
    """

    if len(data) < 1:
        return False
    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        updated_employee = await employees_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_employee:
            return True
        return False


async def delete_employee(id: str) -> bool:
    """
    Удаление сотрудника по ID

    :param id: уникальный ID в бд
    :return:
    """

    employee = await employees_collection.find_one({"_id": ObjectId(id)})
    if employee:
        await employees_collection.delete_one({"_id": ObjectId(id)})
        return True


async def retrieve_employees_by_gender(gender: str) -> list:
    """
    Получение списка сотрудников с фильтрацией по гендеру.

    :param gender: значение гендера (male/female)
    :return: - отфильтрованный список сотрудников
    """

    employees = []

    async for employee in employees_collection.find({"gender": gender}):
        employees.append(employee_helper(employee))
    return employees


async def retrieve_employees_by_company(company: str) -> list:
    """
    Получение списка сотрудников с фильтрацией по компании

    :param company: - название компании
    :return: - отфильтрованный список сотрудников
    """

    employees = []

    async for employee in employees_collection.find({"company": company}):
        employees.append(employee_helper(employee))
    return employees


async def retrieve_employees_by_age(age: int) -> list:
    """
    Получение списка сотрудников с фильтрацией по возрасту

    :param age: - значение возраста для фильтрации
    :return: - отфильтрованный список сотрудников
    """

    employees = []

    async for employee in employees_collection.find({"age": age}):
        employees.append(employee_helper(employee))
    return employees


async def retrieve_employees_by_salary(salary: int, direction: bool) -> list:
    """
    Получение списка сотрудников с фильтрацией по зарплате

    Для фильтрации "больше": direction=True
    Для фильтрации "меньше": direction=False

    :param salary: - значение зарплаты
    :param direction: - направление фильтрации (больше/меньше)
    :return: - отфильтрованный список сотрудников
    """

    employees = []

    if direction:
        async for employee in employees_collection.find(
            {"salary": {"$gte": salary}}
        ):
            employees.append(employee_helper(employee))
    else:
        async for employee in employees_collection.find(
            {"salary": {"$lte": salary}}
        ):
            employees.append(employee_helper(employee))

    return employees
