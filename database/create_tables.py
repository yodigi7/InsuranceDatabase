from database.flask_db import db
from database.Person_Work import PersonWork
from database.Person import Person


def create_tables():
    db.create_all()


if __name__ == '__main__':
    create_tables()
