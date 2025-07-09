from cars.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    price = relationship("Car")

    def __repr__(self):
        return f"Авто (ID: {self.id}, Стоимость: {self.price})"
