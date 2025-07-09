from cars.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    year = Column(Integer, nullable=False)
    power = Column(Integer, nullable=False)
    car = relationship('Salon')

    def __repr__(self):
        return f"Авто (ID: {self.id}, Модель: {self.model}, Год выпуска: {self.year}, Мощность двигателя: {self.power})"
