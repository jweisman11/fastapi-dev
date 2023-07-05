from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

SQLALCHEMY_DATABASE_URL = 'postgresql://docker:docker@localhost:5432/exampledb'

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)


Base = declarative_base()


def get_db() -> Generator:
    """
    TODO: update docstring
    """

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
