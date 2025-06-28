class Car:
    model = ""
    year = ""
    producer = ""
    power = ""
    color = ""
    price = ""

    def __init__(self, model, year, producer, power, color, price):
        self.__model = model
        self.__year = year
        self.__producer = producer
        self.__power = power
        self.__color = color
        self.__price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.__model}\nГод выпуска: {self.__year}\nПроизводитель: {self.__producer}\n"
              f"Мощность двигателя: {self.__power}\nЦвет машины: {self.__color}\nЦена: {self.__price}")
        print("=" * 40)

    def get_car(self):
        return self.__model, self.__year, self.__producer, self.__power, self.__color, self.__price

    def __check_model(s):
        return isinstance(s, (str, float, int))

    def set_model(self, model):
        if Car.__check_model(model):
            self.__model = model
        else:
            print("Введите корректное название модели")

    def __check_prod(p):
        return isinstance(p, str)

    def set_car(self, producer, color):
        if Car.__check_prod(producer) and Car.__check_prod(color):
            self.__producer = producer
            self.__color = color
        else:
            print("Введите корректное название производителя или цвет машины")

    def __check_year(y):
        return isinstance(y, int)

    def set_year(self, year):
        if Car.__check_year(year):
            self.__year = year
        else:
            print("Введите числовое значение года выпуска")

    def __check_power(pow):
        return isinstance(pow, (str, int))

    def set_power(self, power):
        if Car.__check_power(power):
            self.__power = power
        else:
            print("Введите числовое значение мощности двигателя")

    def __check_price(pr):
        return isinstance(pr, (int, float))

    def set_price(self, price):
        if Car.__check_price(price):
            self.__price = price
        else:
            print("Введите числовое значение стоимости")


c1 = Car("X7 M50i", "2021", "BMW", "530 л.с.", "black", "10500000")

c1.print_info()
c1.set_model("OPEL Astra")
c1.set_year(2024)
c1.set_power("140 л.с.")
c1.set_car("OPEL", "white")
c1.set_price(1500000)
print(c1.get_car())


