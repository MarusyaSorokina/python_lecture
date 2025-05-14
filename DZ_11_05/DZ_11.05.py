import math


class Area:
    __count = 0

    @staticmethod
    def geron_area(a, b, c):
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        Area.__count += 1
        return area

    @staticmethod
    def triangle_area(v, h):
        trian_area = 0.5 * v * h
        Area.__count += 1
        return trian_area

    @staticmethod
    def square_area(d):
        sq_area = d**2
        Area.__count += 1
        return sq_area

    @staticmethod
    def rectangle_area(x, f):
        rect_area = x * f
        Area.__count += 1
        return rect_area

    @staticmethod
    def get_count():
        return Area.__count


s1 = Area.geron_area(3, 4, 5)
print(f"Площадь треугольника по формуле Герона: {s1}")
s2 = Area.triangle_area(6, 7)
print(f"Площадь треугольника через основание и высоту: {s2}")
s3 = Area.square_area(7)
print(f"Площадь квадрата: {s3}")
s4 = Area.rectangle_area(2, 6)
print(f"Площадь прямоугольника: {s4}")
print(Area.get_count())
