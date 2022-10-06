import unittest
from datetime import date, datetime

import pytest
from models.user import User

# MongoDB
# class TestUserModel(unittest.TestCase):
#     """UserModel object"""

#     mock_username = "johndoe"
#     mock_username_int = "johndoe12"

#     def test_username_int(self):
#         """username contains integer"""

#         # user object birthdate can be on the same day!
#         with pytest.raises(ValueError):
#             UserModel(username=self.mock_username_int, dateOfBirth=datetime.today())

#     def test_username(self):
#         user = UserModel(username=self.mock_username, dateOfBirth=datetime.today())
#         self.assertEqual(
#             self.mock_username,
#             user.username,
#         )


# PSQL
class TestUser(unittest.TestCase):
    """User object"""

    mock_username = "johndoe"
    mock_username_int = "johndoe12"

    def test_username_int(self):
        """username contains integer"""

        # user object birthdate can be on the same day!
        with pytest.raises(ValueError):
            User(username=self.mock_username_int, dateofbirth=date.today())

    def test_username(self):
        user = User(username=self.mock_username, dateofbirth=date.today())
        self.assertEqual(
            self.mock_username,
            user.username,
        )
