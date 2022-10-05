from datetime import date, datetime

from pydantic import validator

from .base import BaseSchema


# pylint: disable=E0213
class SetUser(BaseSchema):
    """PUT method body schema"""

    dateOfBirth: date

    @validator("dateOfBirth", pre=True)
    def check_birthdate(cls, value):
        """YYYY-MM-DD must be a date before the today date"""
        dateOfBirth = datetime.strptime(value, "%Y-%m-%d")
        if date.today() <= dateOfBirth.date():
            raise ValueError("dateOfBirth must be a date before the today date")
        return dateOfBirth
