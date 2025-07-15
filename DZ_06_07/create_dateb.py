# from tokenize import salon
from cars.database import create_db, Session

from faker import Faker
from cars.buyer import Buyer
from cars.salon import Salon
from cars.car import Car


def create_dateb(load_data=True):
    create_db()
    if load_data:
        _load_data(Session())


def _load_data(session):
    car_model = ['BMW', 'Audi', 'Opel', 'Citroen', 'Saab', 'Toyota', 'Subaru', 'Dodge']
    salon1 = Salon(salon_name='Auto-new')
    salon2 = Salon(salon_name='Japan-car')

    session.add(salon1)
    session.add(salon2)

    for key, im in enumerate(car_model):
        car = Car(car_model=im)
        car.salons.append(salon1)
        if key % 2 == 0:
            car.salons.append(salon2)
        session.add(car)

    faker = Faker('ru_RU')
    salon_list = [salon1, salon2]

    session.commit()

    for _ in range(50):
        fio_name = faker.name().split()
        age = faker.random.randint(20, 50)
        salon = faker.random.choice(salon_list)
        car_m = faker.random.choice(car_model)

        buyer = Buyer(fio_name, age, salon.id, car_m)
        session.add(buyer)

    session.commit()
    session.close()
