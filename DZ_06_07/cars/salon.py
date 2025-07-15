from cars.database import Cars
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Salon(Cars):
    __tablename__ = 'salons'

    id = Column(Integer, primary_key=True)
    salon_name = Column(String(250), nullable=False)

    buyer = relationship('Buyer')

    def __repr__(self):
        return (f"ID: {self.id}, Название: {self.salon_name}")
