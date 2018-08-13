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


def json_to_work(input_json: dict) -> PersonWork:
    query = PersonWork.query.filter(PersonWork.person_id == input_json['person_id'])
    if query.one_or_none():
        return query.one()
    person_work = PersonWork(person_id=input_json['person_id'], occupation=input_json['occupation'],
                             occupation_start=input_json['occupation_start'], employer=input_json['employer'],
                             employer_start=input_json['employer_start'],
                             level_of_education=input_json['level_of_education'])
    person_work.add()
    return person_work


if __name__ == '__main__':
    pass
