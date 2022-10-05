from core import user

# from core.user import get_user_by_username, set_user
from fastapi import APIRouter, Body, Depends, status

# from odmantic import AIOEngine
from schemas.hello import HelloResponse
from schemas.user import SetUser

# from settings import EngineD,
from settings import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/hello/{username}", response_model=HelloResponse, responses={404: {}})
# async def get_hello(
def get_hello(
    username: str,
    engine: Session = Depends(get_db),
    # engine: AIOEngine = EngineD,
):
    """returns hello response with user content"""
    # user = await get_user_by_username(engine, username)
    user_obj = user.get_user_by_username(engine, username)
    return HelloResponse.from_user_instance(user_obj)


@router.put("/hello/{username}", status_code=status.HTTP_204_NO_CONTENT)
# async def create_or_update_user(
def create_or_update_user(
    username: str,
    data: SetUser = Body(..., embed=True, alias="user"),
    engine: Session = Depends(get_db),
    # engine: AIOEngine = EngineD,
):
    """creates or updates user object"""
    # await set_user(engine, username=username, **data.dict())
    user.set_user(engine, username=username, **data.dict())
