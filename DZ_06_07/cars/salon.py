from cars.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Salon(Base):
    __tablename__ = 'salon'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    rating = Column(Integer, nullable=False)
    car = Column(Integer, ForeignKey('car.id'))

    def __init__(self, name, city, rating, id_car):
        self.name = name
        self.city = city
        self.rating = rating
        self.car = id_car

    def __repr__(self):
        return (f"Салон: {self.name}, Авто: {self.car}, Город: {self.city}, Рейтинг: {self.rating})")



