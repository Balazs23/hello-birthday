from datetime import datetime

from fastapi.exceptions import RequestValidationError

# from odmantic import Model
from pydantic import StrictStr, ValidationError, validator
from pydantic.error_wrappers import ErrorWrapper
from settings import Base
from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.sql import func


class User(Base):
    """User ORM Class"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    dateofbirth = Column(Date, nullable=False)
    created_date = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, username, dateofbirth):
        self.username = username
        self.dateofbirth = dateofbirth

    @validates("username")
    def validate_username(self, key, value):
        """username must contain only letters"""
        if not value.isalpha():
            # sqlalchemy and fastapi mixin
            raise RequestValidationError(
                errors=[
                    ErrorWrapper(
                        ValueError("username must contain only letters"), loc="username"
                    )
                ],
            )

        return value


# MONGODB
# pylint: disable=E0213
# class UserModel(Model):
#     """User model"""

#     username: StrictStr
#     dateOfBirth: datetime

#     @validator("username")
#     def check_username(cls, value):
#         """username must contain only letters"""
#         if not value.isalpha():
#             raise ValueError("username must contain only letters")
#         return value
