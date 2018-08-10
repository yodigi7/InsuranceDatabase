from database.flask_db import db


class Person(db.Model):
    __tablename__ = 'people'

    unique_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    middle_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    prefix = db.Column(db.String(10))
    suffix = db.Column(db.String(20))
    address = db.Column(db.String(70))
    mailing_address = db.Column(db.String(70))
    birth_date = db.Column(db.Date())
    height = db.Column(db.String(4))
    weight = db.Column(db.String(4))
    social_security_number = db.Column(db.Integer())
    is_prospect = db.Column(db.Boolean())
    can_use_credit_score = db.Column(db.Boolean())
    work = db.relationship('PersonWork', backref='person')

    def __str__(self):
        return 'Person(unique_id={}, first_name={}, middle_name={}, last_name={}, prefix={}, suffix={}, address={}'\
            .format(self.unique_id, self.first_name, self.middle_name, self.last_name, self.prefix, self.suffix, self.address)

    def __repr__(self):
        return str(self)

    def add_to_database(self) -> None:
        db.session.add(self)
        db.session.commit()


if __name__ == '__main__':
    pass
