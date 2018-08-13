from database.flask_db import db
from database.Person_Work import PersonWork
from database.Person import Person
from database.Person_Notes import PersonNotes


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
