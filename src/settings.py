from typing import Optional

# from odmantic.fastapi import AIOEngineDependency
from pydantic import BaseSettings
from pydantic.types import SecretStr
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class _Settings(BaseSettings):
    SECRET_KEY: SecretStr = (
        "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    )
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    MONGO_URI: Optional[str] = None
    DATABASE_URL: Optional[str] = "sqlite:///test.db"


# Make this a singleton to avoid reloading it from the env everytime
SETTINGS = _Settings()

# MongoDB
# EngineD = AIOEngineDependency(mongo_uri=SETTINGS.MONGO_URI)

# PSQL
engine = create_engine(SETTINGS.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
