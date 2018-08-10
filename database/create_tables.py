from database.flask_db import db


def create_tables():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    create_tables()
