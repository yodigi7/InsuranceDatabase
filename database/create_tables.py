from sqlalchemy import create_engine

from database.base import Base
from database import Person
from database import Person_Work


def create_tables():
    engine = create_engine('sqlite:///insurance_database.db')
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
