from typing import Generator

from core import user
from fastapi import APIRouter, Body, Depends, status
from schemas.hello import HelloResponse
from schemas.user import SetUser
from settings import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()


def get_db() -> Generator[SessionLocal, None, None]:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/hello/{username}", response_model=HelloResponse, responses={404: {}})
def get_hello(
    username: str,
    engine: Session = Depends(get_db),
) -> HelloResponse:
    """returns hello response with user content"""
    user_obj = user.get_user_by_username(engine, username)
    return HelloResponse.from_user_instance(user_obj)


@router.put("/hello/{username}", status_code=status.HTTP_204_NO_CONTENT)
def create_or_update_user(
    username: str,
    data: SetUser = Body(..., embed=True, alias="user"),
    engine: Session = Depends(get_db),
) -> None:
    """creates or updates user object"""
    user.set_user(engine, username=username, **data.dict())
