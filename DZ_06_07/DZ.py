import os

from cars.database import DATABASE_NAME
# import create_database as db_creator

from cars.salon import Salon
from cars.car import Car
from cars.price import Price


if __name__ == '__main__':
    db_is_creator = os.path.exists(DATABASE_NAME)
    # if not db_is_creator:
    #     db_creator.create_database()

