from sqlalchemy import Column, Integer, String, Boolean, Date, Numeric, create_engine
from sqlalchemy.orm import relationship, sessionmaker

from database.base import Base


class Person(Base):
    __tablename__ = 'people'

    unique_id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    middle_name = Column(String(30))
    last_name = Column(String(30))
    prefix = Column(String(10))
    suffix = Column(String(20))
    address = Column(String(70))
    mailing_address = Column(String(70))
    birth_date = Column(Date())
    height = Column(Numeric())
    weight = Column(Numeric())
    social_security_number = Column(Integer())
    is_prospect = Column(Boolean())
    can_use_credit_score = Column(Boolean())
    work = relationship('PersonWork', backref='person')

    def __str__(self):
        return 'Person(unique_id={}, first_name={}, middle_name={}, last_name={}, prefix={}, suffix={}, address={}'\
            .format(self.unique_id, self.first_name, self.middle_name, self.last_name, self.prefix, self.suffix, self.address)

    def __repr__(self):
        return str(self)

    def add_to_database(self) -> None:
        engine = create_engine('sqlite:///insurance_database.db')
        session = sessionmaker(bind=engine)()
        session.add(self)
        session.commit()


if __name__ == '__main__':
    pass
