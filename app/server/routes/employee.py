from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import Optional

from app.server.database import (
    add_employee,
    retrieve_all_employees,
    retrieve_employee,
    update_employee,
    delete_employee,
    retrieve_employees_by_gender,
    retrieve_employees_by_company,
    retrieve_employees_by_age,
    retrieve_employees_by_salary,
)
from app.server.models.employee import (
    ErrorResponseModel,
    ResponseModel,
    EmployeeSchema,
    UpdateEmployeeModel,
)


router = APIRouter()


@router.post("/employee", response_description="Employee data added")
async def add_employee_data(employee: EmployeeSchema = Body(...)):
    """
    Добавление данных одного сотрудника в БД

    :param employee:
    :return:
    """

    employee = jsonable_encoder(employee)
    new_employee = await add_employee(employee)
    return ResponseModel(new_employee, "Employee was added successfully")


@router.get("/employee/{id}", response_description="Employee data retrieved")
async def get_employee_data(id):
    """
    Получение данных одного сотрудника по ID

    :param id:
    :return:
    """

    employee = await retrieve_employee(id)
    if employee:
        return ResponseModel(employee, "Employee data retrieved successfully")
    return ErrorResponseModel(
        "An error occurred.", 404, "Employee doesn't exist."
    )


@router.put("/employee/{id}")
async def update_employee_data(id: str, req: UpdateEmployeeModel = Body(...)):
    """
    Изменение данных одного сотрудника по ID

    :param id:
    :param req:
    :return:
    """

    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_employee = await update_employee(id, req)
    if updated_employee:
        return ResponseModel(
            "Employee with ID: {} name update is successful.".format(id),
            "Employee name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the employee data.",
    )


@router.delete("/employee/{id}",response_description="Employee data delete")
async def delete_employee_data(id: str):
    """
    Удаление сотрудника по ID


    :param id:
    :return:
    """

    deleted_employee = await delete_employee(id)
    if deleted_employee:
        return ResponseModel(
            "Employee with ID: {} removed".format(id),
            "Employee deleted successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "Employee with ID {0} doesn't exist".format(id),
    )


@router.get("/getAllEmployees", response_description="Employees retrieved")
async def get_all_employees():
    """
    Получение списка всех сотрудников

    :return:
    """

    employees = await retrieve_all_employees()
    if employees:
        return ResponseModel(
            employees, "Employees data retrieved successfully"
        )
    return ResponseModel(employees, "Empty list returned")


@router.get(
    "/getEmployeesByGender/{gender}",
    response_description="Employees retrieved",
)
async def get_employees_by_gender(gender):
    """
    Фильтрация по гендеру (параметр в пути)

    :param gender:
    :return:
    """
    employees = await retrieve_employees_by_gender(gender)
    if employees:
        return ResponseModel(
            employees, "Employees data retrieved successfully"
        )
    return ResponseModel(employees, "Empty list returned")


@router.get("/getEmploeesByCompany")
async def get_employees_by_company(company):
    """
    Фильтрация по компании (параметр в запросе)

    :param company:
    :return:
    """

    employees = await retrieve_employees_by_company(company)
    if employees:
        return ResponseModel(
            employees, "Employees data retrieved successfully"
        )
    return ResponseModel(employees, "Empty list returned")


@router.get("/getEmploeesByAge")
async def get_employees_by_age(age: int):
    """
    Фильтрация списка сотрудников по возрасту (параметр в запросе)

    :param age:
    :return:
    """

    employees = await retrieve_employees_by_age(age)
    if employees:
        return ResponseModel(
            employees, "Employees data retrieved successfully"
        )
    return ResponseModel(employees, "Empty list returned")


@router.get("/getEmploeesBySalary")
async def get_employees_by_salary(salary: int, direction: bool = True):
    """
    Фильтрация списка сотрудников по зарплате.

    Принимает два параметра. Значение зарплаты и направление фильтрации.
    Направление по умолчанию = True, "больше или равно"

    :param salary:
    :param direction:
    :return:
    """

    employees = await retrieve_employees_by_salary(salary, direction)
    if employees:
        if direction:
            return ResponseModel(
                employees, "Employees with salary more than {}".format(salary)
            )
        return ResponseModel(
            employees, "Employees with salary less than {}".format(salary)
        )
    return ResponseModel(employees, "Empty list returned")
