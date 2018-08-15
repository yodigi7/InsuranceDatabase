from database.flask_db import db

from database.Person_Work import PersonWork
from database.Person_Notes import PersonNotes
from database.Person_Driving import PersonDrivingViolation, PersonDrivingAccident
from database.Person_Phones import PersonPhone


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
    birth_date = db.Column(db.String(12))
    height = db.Column(db.String(6))
    weight = db.Column(db.String(4))
    social_security_number = db.Column(db.Integer())
    customer_type = db.Column(db.String(20))
    can_use_credit_score = db.Column(db.Boolean())

    note = db.relationship('PersonNotes', backref='person', cascade='delete, delete-orphan')
    work = db.relationship('PersonWork', backref='person', cascade='delete, delete-orphan')
    driving_violations = db.relationship('PersonDrivingViolation', backref='person', cascade='delete, delete-orphan')
    driving_accidents = db.relationship('PersonDrivingAccident', backref='person', cascade='delete, delete-orphan')
    phones = db.relationship('PersonPhone', backref='person', cascade='delete, delete-orphan')

    def __str__(self):
        return 'Person(unique_id={}, first_name={}, middle_name={}, last_name={}, prefix={}, suffix={}, address={}' \
            .format(self.unique_id, self.first_name, self.middle_name, self.last_name, self.prefix, self.suffix,
                    self.address)

    def __repr__(self):
        return str(self)

    @staticmethod
    def update() -> None:
        db.session.commit()

    def add(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

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
            'customer_type': self.customer_type,
            'can_use_credit_score': self.can_use_credit_score,
            'note': [x.to_json_str() for x in self.note],
            'work': [x.to_json() for x in self.work],
            'driving_violations': [x.to_json() for x in self.driving_violations],
            'driving_accidents': [x.to_json() for x in self.driving_accidents]
        }


def create_person(dictionary: dict) -> Person:
    dictionary['weight'] = str(dictionary.get('weight'))
    dictionary['socialSecurityNumber'] = dictionary.get('socialSecurityNumber')
    if dictionary.get('birthDate'):
        dictionary['birthDate'] = dictionary.get('birthDate')
    else:
        dictionary['birthDate'] = None
    return Person(prefix=dictionary.get('prefix'),
                  first_name=dictionary.get('firstName'),
                  middle_name=dictionary.get('middleName'),
                  last_name=dictionary.get('lastName'),
                  suffix=dictionary.get('suffix'),
                  address=dictionary.get('address'),
                  mailing_address=dictionary.get('mailingAddress'),
                  birth_date=dictionary.get('birthDate'),
                  height=dictionary.get('height'),
                  weight=dictionary.get('weight'),
                  social_security_number=dictionary.get('socialSecurityNumber'),
                  customer_type=dictionary.get('customerType'),
                  can_use_credit_score=dictionary.get('canUseCreditScore'))


def json_to_person(input_json: dict) -> Person:
    person = create_person(input_json)
    return person


if __name__ == '__main__':
    pass
