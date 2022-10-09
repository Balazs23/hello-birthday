from pydantic.main import BaseModel


# pylint: disable=C0115
class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
