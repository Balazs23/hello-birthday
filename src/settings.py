import os
from typing import Optional

import pg8000
from google.cloud.sql.connector import Connector, IPTypes

# from odmantic.fastapi import AIOEngineDependency
from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class _Settings(BaseSettings):
    if os.environ.get("K_SERVICE"):
        # gcp cloud run instance
        INSTANCE_CONNECTION_NAME: str  # 'project:region:instance'
        DB_IAM_USER: str  # alias@project.iam
        DB_NAME: str
        PRIVATE_IP: Optional[str] = None
    else:
        DATABASE_URL: Optional[str] = "sqlite:///test.db"


# Make this a singleton to avoid reloading it from the env everytime
SETTINGS = _Settings()

# MongoDB
# EngineD = AIOEngineDependency(mongo_uri=SETTINGS.MONGO_URI)

# PSQL


def getconn() -> pg8000.dbapi.Connection:
    """cloud sql connector settings"""
    with Connector() as connector:
        conn = connector.connect(
            SETTINGS.INSTANCE_CONNECTION_NAME,
            "pg8000",
            user=SETTINGS.DB_IAM_USER,
            db=SETTINGS.DB_NAME,
            enable_iam_auth=True,
            ip_type=IPTypes.PUBLIC,  # IPTypes.PRIVATE for private IP
        )
    return conn


if os.environ.get("K_SERVICE"):
    # https://cloud.google.com/run/docs/container-contract#services-env-vars
    engine = create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )
else:
    engine = create_engine(SETTINGS.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
