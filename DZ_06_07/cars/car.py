from cars.database import Cars
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('association', Cars.metadata,
                          Column('car_id', Integer, ForeignKey('cars.id')),
                          Column('salon_id', Integer, ForeignKey('salons.id')))


class Car(Cars):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    car_model = Column(String(250), nullable=False)
    salons = relationship("Salon", secondary=association_table,
                          backref='salon_car')

    def __repr__(self):
        return (f"Авто (ID: {self.id}, Модель: {self.car_model}")

