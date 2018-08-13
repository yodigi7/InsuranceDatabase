from database.flask_db import db


class PersonWork(db.Model):
    __tablename__ = 'people_work'

    person_id = db.Column(db.Integer, db.ForeignKey('people.unique_id'), primary_key=True)
    occupation = db.Column(db.String(50))
    occupation_start = db.Column(db.Date())
    employer = db.Column(db.String(50))
    employer_start = db.Column(db.Date())
    level_of_education = db.Column(db.String(20))
    person = db.relationship('Person', backref='work')

    def add_to_database(self) -> None:
        db.session.add(self)
        db.session.commit()

    def to_json(self) -> dict:
        return {
            'person_id': self.person_id,
            'occupation': self.occupation,
            'occupation_start': self.occupation_start,
            'employer': self.employer,
            'employer_start': self.employer_start,
            'level_of_education': self.level_of_education
        }


if __name__ == '__main__':
    pass
