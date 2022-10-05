from datetime import date

from models.user import User

from .base import BaseSchema


class HelloResponse(BaseSchema):
    """Hello endpoint response schema"""

    message: str

    @classmethod
    def from_user_instance(cls, user: User) -> "HelloResponse":
        """returns hello message based on birthday"""
        if date.today() == user.dateofbirth:
            # it is birthday!!!
            return cls(message=f"Hello, {user.username}! Happy birthday!")

        # non birthday message
        td = date.today() - user.dateofbirth
        return cls(
            message=f"Hello, {user.username}! Your birthday is in {td.days} day(s)"
        )
