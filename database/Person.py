from database.flask_db import db

from database.Person_Work import PersonWork
from database.Person_Notes import PersonNotes
from database.Person_Driving import PersonDrivingViolation, PersonDrivingAccident


class Person(db.Model):
    __tablename__ = 'people'

    unique_id = db.Column(db.Integer(), primary_key=True)
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

    driving_violations = db.relationship('PersonDrivingViolation', backref='person')
    driving_accidents = db.relationship('PersonDrivingAccident', backref='person')

    def __str__(self):
        return 'Person(unique_id={}, first_name={}, middle_name={}, last_name={}, prefix={}, suffix={}, address={}'\
            .format(self.unique_id, self.first_name, self.middle_name, self.last_name, self.prefix, self.suffix, self.address)

    def __repr__(self):
        return str(self)

    def to_json(self):
        return {
            'unique_id': self.unique_id,
            'prefix': self.prefix,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'suffix': self.suffix,
            'address': self.address,
            'mailing_address': self.mailing_address,
            'birth_date': self.birth_date,
            'height': self.height,
            'weight': self.weight,
            'social_security_number': self.social_security_number,
            'is_prospect': self.is_prospect,
            'can_use_credit_score': self.can_use_credit_score,
            'notes': [x.to_json for x in self.notes],
            'work': [x.to_json for x in self.work],
            'driving_violations': [x.to_json for x in self.driving_violations],
            'driving_accidents': [x.to_json for x in self.driving_accidents]
        }

    @staticmethod
    def update() -> None:
        db.session.commit()

    def add(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


if __name__ == '__main__':
    pass
