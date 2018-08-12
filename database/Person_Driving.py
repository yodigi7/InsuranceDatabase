from database.flask_db import db


class PersonDrivingViolation(db.Model):
    __tablename__ = 'person_driving_violation'

    unique_id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('people.unique_id'))
    date_received = db.Column(db.Date())
    date_convicted = db.Column(db.Date())
    type = db.Column(db.Text())

    def __str__(self):
        return 'Person(unique_id={}, person_id={}, date_received={}, date_convicted={}, type={}'\
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


class PersonDrivingAccident(db.Model):
    __tablename__ = 'person_driving_accident'

    unique_id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey('people.unique_id'))
    percent_fault = db.Column(db.Numeric(3))
    injuries = db.Column(db.Integer())
    description = db.Column(db.Text())
    paid_by = db.Column(db.String(70))

    def __str__(self):
        return 'Person(unique_id={}, person_id={}, date_received={}, date_convicted={}, type={}'\
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


if __name__ == '__main__':
    pass
