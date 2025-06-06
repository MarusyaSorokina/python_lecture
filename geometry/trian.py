class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    t1 = Triangle(1, 2, 3)
    t2 = Triangle(4, 5, 6)
    print(t1.perimeter())
    print(t2.perimeter())
