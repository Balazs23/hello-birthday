import unittest
from datetime import date, timedelta

import pytest
from dateutil.relativedelta import relativedelta
from models.user import User
from schemas.hello import HelloResponse
from schemas.user import SetUser


class TestHelloSchema(unittest.TestCase):
    """Hello HTTP Response schema"""

    mock_username = "johndoe"
    timedelta = 1
    days_of_year = 365  # edge case leap year!

    def test_hello_birthday(self) -> None:
        """birthday day"""
        hello = HelloResponse.from_user_instance(
            User(username=self.mock_username, dateofbirth=date.today())
        )

        self.assertEqual(hello.message, f"Hello, {self.mock_username}! Happy birthday!")

    def test_hello_birthday_years(self) -> None:
        """birthday was years ago"""
        hello = HelloResponse.from_user_instance(
            User(
                username=self.mock_username,
                dateofbirth=(date.today() - relativedelta(years=self.timedelta)),
            )
        )

        self.assertEqual(hello.message, f"Hello, {self.mock_username}! Happy birthday!")

    def test_hello_not_birthday(self) -> None:
        """non birthday day"""
        hello = HelloResponse.from_user_instance(
            User(
                username="johndoe",
                dateofbirth=(date.today() - timedelta(days=self.timedelta)),
            )
        )

        self.assertEqual(
            hello.message,
            f"Hello, {self.mock_username}! Your birthday is in {self.days_of_year - self.timedelta} day(s)",  # noqa: E501
        )

    def test_hello_not_birthday_years(self) -> None:
        """non birthday day"""
        hello = HelloResponse.from_user_instance(
            User(
                username="johndoe",
                dateofbirth=(
                    date.today()
                    - timedelta(days=self.timedelta)
                    - relativedelta(years=self.timedelta)
                ),
            )
        )

        self.assertEqual(
            hello.message,
            f"Hello, {self.mock_username}! Your birthday is in {self.days_of_year - self.timedelta} day(s)",  # noqa: E501
        )


class TestSetUserSchema(unittest.TestCase):
    """SetUser HTTP Request schema"""

    wrong_date_formats = [
        "%Y/%m/%d",
        "%Y.%m.%d",
        "%m.%d.%Y",
        "%m/%d/%Y",
        "%m-%d-%Y",
    ]

    date_format = "%Y-%m-%d"

    def test_wrong_date_format(self) -> None:
        """wrong date() formats"""

        for wrong in self.wrong_date_formats:
            with pytest.raises(ValueError):
                dt = date.today() - timedelta(days=1)
                SetUser(dateOfBirth=dt.strftime(wrong))

    def test_date_today(self) -> None:
        """can not set current day as birthday"""
        with pytest.raises(ValueError):
            dt = date.today()
            SetUser(dateOfBirth=dt.strftime(self.date_format))

    def test_date(self) -> None:
        dt = date.today() - timedelta(days=1)
        request = SetUser(dateOfBirth=dt.strftime(self.date_format))
        self.assertEqual(
            dt,
            request.dateOfBirth,
        )
