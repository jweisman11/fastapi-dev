from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from datetime import date


Agency = Enum(
    value="Agency",
    names=[
        ("CBP", "CBP"),
        ("ICE", "ICE"),
        ("I&A", "I&A"),
        ("USCIS", "USCIS"),
    ],
)


class User(BaseException):
    """
    Pydantic data model (schema) to CRUD API requests for users
    """

    name: str = Field(default=None, title="Full name of user", max_length=100)
    email: EmailStr()
    agency: Agency
    date_added: date = Field(default=date.today(), title="Date added")
    super_user: bool = Field(default=False)
