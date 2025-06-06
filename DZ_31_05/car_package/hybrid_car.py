from car_package.car import Car


class HybridCar(Car):
    def __init__(self, brand, model, year, mileage, battery_capacity, fuel_consumption):
        super().__init__(brand, model, year, mileage)
        self._validate_hybrid_params(battery_capacity, fuel_consumption)
        self.battery_capacity = battery_capacity
        self.fuel_consumption = fuel_consumption

    def _validate_hybrid_params(self, battery_capacity, fuel_consumption):
        if not isinstance(battery_capacity, (int, float)):
            raise ValueError("Емкость батареи должна быть числом.")

        if battery_capacity < 0 or battery_capacity > 100:
            raise ValueError("Заряд батареи должен быть между 0 и 100%.")

        if not isinstance(fuel_consumption, (int, float)):
            raise ValueError("Расход топлива должен быть числом.")

        if fuel_consumption <= 0 or fuel_consumption > 30:
            raise ValueError("Расход топлива должен быть между 0 и 30 л/100км")

    def get_power_source(self):
        if self.battery_capacity > 20:
            return "электрический"
            return "бензиновый"

    def print_info(self):
        super().print_info()
        print(f"Тип: гибрид, заряд батареи: {self.battery_capacity}%, "
              f"расход топлива: {self.fuel_consumption} л/100км")
