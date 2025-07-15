import os

from cars.database import DATABASE_NAME
import create_dateb as db_creator

if __name__ == '__main__':
    db_car_creator = os.path.exists(DATABASE_NAME)
    if not db_car_creator:
        db_creator.create_dateb()

