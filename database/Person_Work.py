from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

from database.base import Base


class PersonWork(Base):
    __tablename__ = 'people_work'

    person_id = Column(Integer, ForeignKey('people.unique_id'), primary_key=True)
    occupation = Column(String(50))
    occupation_start = Column(Date())
    employer = Column(String(50))
    employer_start = Column(Date())
    level_of_education = Column(String(20))

    def add_to_database(self) -> None:
        engine = create_engine('sqlite:///insurance_database.db')
        session = sessionmaker(bind=engine)()
        session.add(self)
        session.commit()


if __name__ == '__main__':
    pass
