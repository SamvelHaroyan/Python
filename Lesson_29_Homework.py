from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def perimetr(self):
        ...

    @abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, r):
        if r > 0:
            self.r = r
        else:
            raise ValueError

    def perimetr(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * (self.r ** 2)


class Rectangle(Shape):
    def __init__(self, a, b):
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else:
            raise ValueError

    def perimetr(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Triangle(Shape):
    def __init__(self, a, b=0, c=0, h=0, ankyun=0):
        if a <= 0 and b <= 0 and c <= 0 and h <= 0 and ankyun == 0:
            raise ValueError
        if ankyun < 0 or ankyun >= 180:
            raise ValueError

        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.ankyun = ankyun

    def perimetr(self):
        if self.b > 0 and self.c > 0:
            return self.a + self.b + self.c
        else:
            raise ValueError

    def area(self):
        if self.b > 0 and self.c > 0:
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        elif self.h > 0:
            return 0.5 * self.a * self.h
        elif self.ankyun > 0:
            return 0.5 * self.a * self.b * math.sin(self.ankyun)
        else:
            raise ValueError


# c1 = Circle(-1)  # Value error test
c2 = Circle(5)
print("Perimeter:", c2.perimetr())
print("Area:", c2.area())

r1 = Rectangle(3, 4)
print("Perimeter:", r1.perimetr())
print("Area:", r1.area())

t1 = Triangle(3, 4, 5)
print("Perimeter:", t1.perimetr())
print("Area with 3 sides:", t1.area())

t2 = Triangle(5, h=6)
print("Area with side and height:", t2.area())

t3 = Triangle(5, 6, ankyun=30)
print("Area with two sides and angle:", t3.area())
