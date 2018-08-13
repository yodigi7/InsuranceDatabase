from database.flask_db import db


class PersonNotes(db.Model):
    __tablename__ = 'people_note'

    person_id = db.Column(db.Integer, db.ForeignKey('people.unique_id'), primary_key=True)
    note = db.Column(db.Text())
    person = db.relationship('Person', backref='note')

    def __str__(self):
        return 'Person(person_id={}, note={}'.format(self.person_id, self.note)

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

    def to_json_str(self) -> str:
        return self.note


def json_to_note(input_json: dict) -> PersonNotes:
    query = PersonNotes.query.filter(PersonNotes.person_id == input_json['person_id'])
    if query.one_or_none():
        return query.one()
    person_notes = PersonNotes(person_id=input_json['person_id'], note=input_json['note'])
    person_notes.add()
    return person_notes


if __name__ == '__main__':
    pass
