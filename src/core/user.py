from datetime import date

from models.user import User

# from odmantic import AIOEngine
from sqlalchemy.orm import Session

from core.exceptions import InvalidValueException, UserNotFoundException

# async def get_user_by_username(engine: AIOEngine, username: str) -> UserModel:
#     """returns user object based on username"""
#     user = await engine.find_one(UserModel, UserModel.username == username)
#     if user is None:
#         raise UserNotFoundException()
#     return user


def get_user_by_username(engine: Session, username: str) -> User:
    """returns user object based on username"""
    user = engine.query(User).filter(User.username == username).first()
    if user is None:
        raise UserNotFoundException()
    return user


# type: ignore
# pylint: disable=E1101
# async def set_user(engine: AIOEngine, username: str, dateOfBirth: date):
#     """create or update user object"""
#     try:
#         user = await engine.find_one(UserModel, UserModel.username == username)
#         # covert date to datetime type for mongodb
#         birth_datetime = datetime.combine(dateOfBirth, datetime.min.time())
#         if user is None:
#             # create user
#             user = UserModel(username=username, dateOfBirth=birth_datetime)
#         else:
#             # update current user
#             setattr(user, "dateOfBirth", birth_datetime)
#         await engine.save(user)
#     except ValueError as err:
#         raise InvalidValueException(err.errors()) from err


def set_user(engine: Session, username: str, dateOfBirth: date):
    """create or update user object"""
    try:
        user = engine.query(User).filter(User.username == username).first()
        if user is None:
            # create user
            user = User(username=username, dateofbirth=dateOfBirth)
            engine.add(user)
        else:
            # update current user
            user.dateofbirth = dateOfBirth
        engine.commit()
        engine.refresh(user)
    except ValueError as err:
        raise InvalidValueException(err.errors()) from err
