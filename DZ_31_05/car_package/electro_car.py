from car_package.car import Car


class ElectroCar(Car):
    def __init__(self, brand, model, year, mileage, battery_capacity=100):
        super().__init__(brand, model, year, mileage)
        self._validate_input(battery_capacity)
        self.battery_capacity = battery_capacity

    def info(self):
        print(f"Заряд батареи: {self.battery_capacity}%.")

    def print_info(self):
        super().print_info()
        print(f"Заряд батареи: {self.battery_capacity}%.")

    def _validate_input(self, capacity):
        if not isinstance(capacity, (int, float)):
            raise ValueError("Заряд батареи должен быть числом.")

        if capacity < 0 or capacity > 100:
            raise ValueError("Заряд батареи должен быть между 0 и 100%.")



