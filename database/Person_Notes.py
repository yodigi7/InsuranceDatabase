from database.flask_db import db


class PersonNotes(db.Model):
    __tablename__ = 'people_notes'

    person_id = db.Column(db.Integer, db.ForeignKey('people.unique_id'), primary_key=True)
    notes = db.Column(db.Text())
    person = db.relationship('Person', backref='notes')

    def __str__(self):
        return 'Person(person_id={}, notes={}'.format(self.person_id, self.notes)

    def __repr__(self):
        return str(self)

    def update(self) -> None:
        db.session.commit()

    def add(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


if __name__ == '__main__':
    pass
