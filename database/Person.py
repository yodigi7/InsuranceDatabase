from database import Person_Notes, Person_Driving, Person_Work
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
            'is_prospect': self.is_prospect,
            'can_use_credit_score': self.can_use_credit_score,
            'note': [x.to_json_str() for x in self.note],
            'work': [x.to_json() for x in self.work],
            'driving_violations': [x.to_json() for x in self.driving_violations],
            'driving_accidents': [x.to_json() for x in self.driving_accidents]
        }


def create_person(dictionary: dict) -> Person:
    if 'unique_id' in dictionary.keys():
        return Person(unique_id=dictionary.get('unique_id'),
                      prefix=dictionary.get('prefix'),
                      first_name=dictionary.get('first_name'),
                      middle_name=dictionary.get('middle_name'),
                      last_name=dictionary.get('last_name'),
                      suffix=dictionary.get('suffix'),
                      address=dictionary.get('address'),
                      mailing_address=dictionary.get('mailing_address'),
                      birth_date=dictionary.get('birth_date'),
                      height=dictionary.get('height'),
                      weight=dictionary.get('weight'),
                      social_security_number=dictionary.get('social_security_number'),
                      is_prospect=dictionary.get('is_prospect'),
                      can_use_credit_score=dictionary.get('can_use_credit_score'),
                      note=[x.Person_Notes.json_to_note() for x in dictionary.get('note')],
                      work=[x.Person_Work.json_to_work() for x in dictionary.get('work')],
                      driving_accidents=[Person_Driving.json_to_accident(x) for x in
                                         dictionary.get('driving_accidents')],
                      driving_violations=[Person_Driving.json_to_violation(x) for x in
                                          dictionary.get('driving_violations')])
    return Person(prefix=dictionary.get('prefix'),
                  first_name=dictionary.get('first_name'),
                  middle_name=dictionary.get('middle_name'),
                  last_name=dictionary.get('last_name'),
                  suffix=dictionary.get('suffix'),
                  address=dictionary.get('address'),
                  mailing_address=dictionary.get('mailing_address'),
                  birth_date=dictionary.get('birth_date'),
                  height=dictionary.get('height'),
                  weight=dictionary.get('weight'),
                  social_security_number=dictionary.get('social_security_number'),
                  is_prospect=dictionary.get('is_prospect'),
                  can_use_credit_score=dictionary.get('can_use_credit_score'),
                  note=[x.Person_Notes.json_to_note() for x in dictionary.get('note')],
                  work=[x.Person_Work.json_to_work() for x in dictionary.get('work')],
                  driving_accidents=[Person_Driving.json_to_accident(x) for x in
                                     dictionary.get('driving_accidents')],
                  driving_violations=[Person_Driving.json_to_violation(x) for x in
                                      dictionary.get('driving_violations')])


def json_to_person(input_json: dict) -> Person:
    if 'unique_id' in input_json.keys():
        return Person.query.filter(Person.unique_id == input_json['unique_id']).one()
    person = create_person(input_json)
    person.add()
    return person


if __name__ == '__main__':
    pass
