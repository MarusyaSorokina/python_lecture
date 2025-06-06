class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def print_info(self):
        print(f"{self.brand}, {self.model}, {self.year}, пробег: {self.mileage} км.")

    def _validate_input(self, brand, model, year, mileage):
        if not isinstance(brand, str) or not brand:
            raise ValueError("Марка должна быть не пустой строкой")

        if not isinstance(model, str) or not model:
            raise ValueError("Модель должна быть не пустой строкой")

        if not isinstance(year, int) or year < 1990 or year > 2025:
            raise ValueError("Год должен быть целым числом между 1990 и 2025 годами.")

        if not isinstance(mileage, (int, float)):
            raise ValueError("Пробег должен быть числом.")



