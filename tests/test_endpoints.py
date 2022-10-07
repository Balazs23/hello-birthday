from datetime import date, timedelta
from typing import Any

import pytest
from core import exceptions, user
from mock import MagicMock
from models.user import User
from sqlalchemy.orm import Session
from starlette.testclient import TestClient


def test_get_user(test_app: TestClient, monkeypatch: Any) -> None:
    """GET request return code"""
    mock_user = User(username="johndoe", dateofbirth=date.today())

    def mock_get_user_by_username(engine: Session, username: str) -> User:
        return mock_user

    monkeypatch.setattr(user, "get_user_by_username", mock_get_user_by_username)

    response = test_app.get("/hello/johndoe")
    assert response.status_code == 200


def test_set_user(test_app: TestClient, monkeypatch: Any) -> None:
    """PUT request return code"""

    def mock_set_user(engine: Session, username: str, dateOfBirth: date) -> None:
        return None

    monkeypatch.setattr(user, "set_user", mock_set_user)

    response = test_app.put("/hello/johndoe")
    assert response.status_code == 422


def test_get_user_not_found() -> None:
    """non exsiting user"""
    engine = MagicMock()
    engine.query.return_value.filter.return_value.first.return_value = None
    with pytest.raises(exceptions.UserNotFoundException):
        user.get_user_by_username(engine, "johndoe")


def test_set_new_user() -> None:
    """create a new user"""
    mock_user = User("johndoe", date.today())
    engine = MagicMock()
    engine.query.return_value.filter.return_value.first.return_value = None

    user.set_user(engine, username="johndoe", dateOfBirth=date.today())
    called_obj = engine.add.call_args[0][0]
    assert called_obj.username == mock_user.username
    assert called_obj.dateofbirth == mock_user.dateofbirth


def test_set_update_user() -> None:
    """update an existing users birthdate"""
    mock_user = User("johndoe", date.today() - timedelta(days=1))
    engine = MagicMock()
    engine.query.return_value.filter.return_value.first.return_value = mock_user

    user.set_user(engine, username="johndoe", dateOfBirth=date.today())
    called_obj = engine.refresh.call_args[0][0]
    assert called_obj.dateofbirth == date.today()


def test_set_invalid_user() -> None:
    """username can contain only letters"""
    engine = MagicMock()
    engine.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(exceptions.InvalidValueException):
        user.set_user(engine, username="johndoe1", dateOfBirth=date.today())
