class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        else:
            self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec

    def __lt__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec

    def __le__(self, other):
        return not self.__ge__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.sec // 3600) % 24
        if item == "min":
            return (self.sec // 60) % 60
        if item == "sec":
            return self.sec % 60

        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24

        if key == "hour":
            self.sec = s + 60 * m + value * 3600

        if key == "min":
            self.sec = s + 60 * value + h * 3600

        if key == "sec":
            self.sec = value + 60 * m + h * 3600


c1 = Clock(600)
c2 = Clock(800)
# c2 = 200
# c4 = Clock(300)
# c1 += c2
# c1 -= c2
# c3 = c2 - c1
# c4 = c1 * c2
# c5 = c1 // c2
# c1 //= c2
# c6 = c1 % c2
# c3 = c1 + c2 + c4

print(c1.get_format_time())
print(c2.get_format_time())
# print(c3.get_format_time())
# print(c4.get_format_time())
# print(c5.get_format_time())
# print(c6.get_format_time())

# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 14
# c1["min"] = 20
# c1["sec"] = 50
# print(c1.get_format_time())

# print(c2.get_format_time())
# print(c3.get_format_time())
# print(c4.get_format_time())
#
# if c1 == c2:
#     print("Время одинаковое")
# else:
#     print("Время разное")
#
# if c1 != c2:
#     print("Время разное ")
# else:
#     print("Время одинаковое")

# if c1 > c2:
#     print("c1 > c2 True")
# else:
#     print("False")
#
# if c1 < c2:
#     print("c1 < c2 False")
# else:
#     print("True")

if c1 >= c2:
    print("c1 >= c2 True")
else:
    print("False")

if c1 <= c2:
    print("c1 <= c2 True")
else:
    print("False")
