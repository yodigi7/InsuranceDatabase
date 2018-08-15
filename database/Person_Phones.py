from database.flask_db import db


class PersonPhone(db.Model):
    __tablename__ = 'person_phone'

    unique_id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('people.unique_id'))
    phone_number = db.Column(db.Integer())
    type = db.Column(db.String(15))

    def __str__(self):
        return 'PersonPhone(unique_id={}, person_id={}, phone_number={}, type={}' \
            .format(self.unique_id, self.person_id, self.phone_number, self.type)

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
            'person_id': self.person_id,
            'phone_number': self.phone_number,
            'type': self.type,
        }


def create_person_phone(dictionary: dict) -> PersonPhone:
    return PersonPhone(person_id=dictionary.get('personId'),
                       phone_number=dictionary.get('phoneNumber'),
                       type=dictionary.get('type'))


def json_to_phone(input_json: dict) -> PersonPhone:
    person_phone = create_person_phone(input_json)
    return person_phone


if __name__ == '__main__':
    pass
