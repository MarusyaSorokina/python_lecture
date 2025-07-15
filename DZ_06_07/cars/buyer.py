from cars.database import Cars
from sqlalchemy import Column, Integer, String, ForeignKey


class Buyer(Cars):
    __tablename__ = "buyer"

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    age = Column(Integer)
    car = Column(String(250), nullable=False)
    salon = Column(Integer, ForeignKey('salons.id'))

    def __init__(self, fio_name, age, id_salon, car):
        self.surname = fio_name[0]
        self.name = fio_name[1]
        self.age = age
        self.salon = id_salon
        self.car = car

    def __repr__(self):
        return (f"Покупатель (ФИО: {self.surname} {self.name}"
                f"Возраст: {self.age}, ID автосалона: {self.salon}, Авто: {self.car}")
