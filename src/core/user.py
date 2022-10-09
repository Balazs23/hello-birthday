from datetime import date

from models.user import User

# from odmantic import AIOEngine
from sqlalchemy.orm import Session

from core.exceptions import InvalidValueException, UserNotFoundException


def get_user_by_username(engine: Session, username: str) -> User:
    """returns user object based on username"""
    user = engine.query(User).filter(User.username == username).first()
    if user is None:
        raise UserNotFoundException()
    return user


# pylint: disable=E1101
def set_user(engine: Session, username: str, dateOfBirth: date) -> None:
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
