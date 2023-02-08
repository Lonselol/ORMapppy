from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DATABASE_NAME = 'ORMdb'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
session = Session(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
