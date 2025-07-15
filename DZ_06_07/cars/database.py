from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_NAME = 'auto.db'

base = create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(bind=base)
Cars = declarative_base()


def create_db():
    Cars.metadata.create_all(base)
