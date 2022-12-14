import unittest
from datetime import date

import pytest
from models.user import User


# PSQL
class TestUser(unittest.TestCase):
    """User object"""

    mock_username = "johndoe"
    mock_username_int = "johndoe12"

    def test_username_int(self) -> None:
        """username contains integer"""

        # user object birthdate can be on the same day!
        with pytest.raises(ValueError):
            User(username=self.mock_username_int, dateofbirth=date.today())

    def test_username(self) -> None:
        """testing with correct username"""
        user = User(username=self.mock_username, dateofbirth=date.today())
        self.assertEqual(
            self.mock_username,
            user.username,
        )
