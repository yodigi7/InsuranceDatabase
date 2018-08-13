from database.flask_db import db


class PersonDrivingViolation(db.Model):
    __tablename__ = 'person_driving_violation'

    unique_id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('people.unique_id'))
    date_received = db.Column(db.Date())
    date_convicted = db.Column(db.Date())
    type = db.Column(db.Text())

    def __str__(self):
        return 'Person(unique_id={}, person_id={}, date_received={}, date_convicted={}, type={}' \
            .format(self.unique_id, self.person_id, self.date_received, self.date_convicted, self.type)

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

    def to_json(self) -> dict:
        return {
            'unique_id': self.unique_id,
            'person_id': self.person_id,
            'date_received': self.date_received,
            'date_convicted': self.date_convicted,
            'type': self.type
        }


class PersonDrivingAccident(db.Model):
    __tablename__ = 'person_driving_accident'

    unique_id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('people.unique_id'))
    percent_fault = db.Column(db.Numeric(3))
    date_occurred = db.Column(db.Date())
    injuries = db.Column(db.Integer())
    description = db.Column(db.Text())
    paid_by = db.Column(db.String(70))

    def __str__(self):
        return 'Person(unique_id={}, person_id={}, date_received={}, date_convicted={}, type={}' \
            .format(self.unique_id, self.person_id, self.date_received, self.date_convicted, self.type)

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

    def to_json(self) -> dict:
        return {
            'unique_id': self.unique_id,
            'person_id': self.person_id,
            'date_occurred': self.date_occurred,
            'percent_fault': self.percent_fault,
            'injuries': self.injuries,
            'description': self.description,
            'paid_by': self.paid_by
        }


def json_to_accident(input_json: dict) -> PersonDrivingAccident:
    query = PersonDrivingAccident.query.filter(PersonDrivingAccident.unique_id == input_json['unique_id'])
    if query.one_or_none():
        return query.one()
    person_driving_accident = PersonDrivingAccident(unique_id=input_json.get('unique_id'),
                                                    person_id=input_json.get('unique_id'),
                                                    date_occurred=input_json.get('date_occurred'),
                                                    percent_fault=input_json.get('percent_fault'),
                                                    injuries=input_json.get('injuries'),
                                                    description=input_json.get('description'),
                                                    paid_by=input_json.get('paid_by'))
    person_driving_accident.add()
    return person_driving_accident


def json_to_violation(input_json: dict) -> PersonDrivingViolation:
    query = PersonDrivingViolation.query.filter(PersonDrivingViolation.unique_id == input_json['unique_id'])
    if query.one_or_none():
        return query.one()
    person_driving_violation = PersonDrivingViolation(unique_id=input_json.get('unique_id'),
                                                      person_id=input_json.get('person_id'),
                                                      date_received=input_json.get('date_received'),
                                                      date_convicted=input_json.get('date_convicted'),
                                                      type=input_json.get('type'))
    person_driving_violation.add()
    return person_driving_violation


if __name__ == '__main__':
    pass
