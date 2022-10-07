from datetime import date
from typing import Any

from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ErrorWrapper
from settings import Base
from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.sql import func


class User(Base):  # type: ignore
    """User ORM Class"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    dateofbirth = Column(Date, nullable=False)
    created_date = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, username: str, dateofbirth: date):
        self.username = username
        self.dateofbirth = dateofbirth

    @validates("username")  # type: ignore
    def validate_username(self, key: Any, value: Any) -> Any:
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
