from datetime import date

from models.user import User

from .base import BaseSchema


class HelloResponse(BaseSchema):
    """Hello endpoint response schema"""

    message: str

    @classmethod
    def from_user_instance(cls, user: User) -> "HelloResponse":
        """returns hello message based on birthday"""

        def calculate_dates(birthday: date) -> int:
            """calculates birthday in current year"""
            now = date.today()
            delta1 = date(now.year, birthday.month, birthday.day)
            delta2 = date(now.year + 1, birthday.month, birthday.day)
            days_left = ((delta1 if delta1 >= now else delta2) - now).days
            return abs(days_left)

        delta = calculate_dates(user.dateofbirth)
        if delta == 0:
            # it is birthday!!!
            return cls(message=f"Hello, {user.username}! Happy birthday!")

        # non birthday message
        return cls(
            message=f"Hello, {user.username}! Your birthday is in {delta} day(s)"
        )
