from car_package import __all__
from car_package.car import Car
from car_package.electro_car import ElectroCar
from car_package.hybrid_car import HybridCar

try:

    cars = [
        Car("Opel", "Zafira B", 2008, 180000),
        ElectroCar("Nissan", "Leaf", 2021, 40000, 90),
        HybridCar("Toyota", "Prius", 2022, 50000, 75, 4.7)
    ]

    for car in cars:
        car.print_info()
        if isinstance(car, HybridCar):
            print(f"Текущий источник питания: {car.get_power_source()}")
        print("-" * 40)


except ValueError as e:
    print(f"Ошибка: {e}")