from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class EmployeeSchema(BaseModel):

    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0)
    company: str = Field(...)
    join_date: str = Field(...)
    job_title: str = Field(...)
    gender: str = Field(...)
    salary: int = Field(..., gt=0)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "age": 40,
                "company": "Company",
                "join_date": "2010-10-10T18:18:10-08:00",
                "job_title": "employee",
                "gender": "male",
                "salary": 5000,
            }
        }


class UpdateEmployeeModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]
    company: Optional[str]
    join_date: Optional[str]
    job_title: Optional[str]
    gender: Optional[str]
    salary: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "age": 40,
                "company": "Company",
                "join_date": "2010-10-10T18:18:10-08:00",
                "job_title": "employee",
                "gender": "male",
                "salary": 5000,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
