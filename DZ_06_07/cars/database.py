from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


DATABASE_NAME = 'auto.db'

base = create_engine(f"sqlite:///{DATABASE_NAME}")
Base = declarative_base()


def create_db():
    Base.metadata.create_all(base)
