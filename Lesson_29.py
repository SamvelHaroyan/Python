class Car:
    """Model of car"""

    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.mileage_ = 0
        print('Car is created!')

    def description(self):
        """Get description of car."""
        return f'{self.year} {self.company} {self.model}'

    def mileage(self):
        """Get mileage."""
        return f'Mileage: {self.mileage_}'

    def go(self, km):
        self.mileage_ += km
        print(f'My {self.company} drove {km} km.')


# c1 = Car('Mercedes', "C", 1998)
# print(c1.description())
# c1.go(200)
# c1.go(50)
# print(c1.mileage())


class ElectricCar(Car):
    def __init__(self, company, model, year, bat):
        # Car.__init__(self, company, model, year)
        super().__init__(company, model, year)
        self.bat = bat

    def desc_battery(self):
        return f'Battery: {self.bat}%'

    def go(self, km):
        km_pos = self.bat * 2
        if km_pos >= km:
            self.mileage_ += km
            self.bat -= km / 2
            print(f'My {self.company} drove {km} km, battery: {self.bat}%.')
        else:
            self.mileage_ += km_pos
            self.bat = 0
            print(f'My {self.company} drove {km_pos} km, battery: {self.bat}%.')
            print('Battery is low.')


# c1 = ElectricCar('Tesla', "S", 2020, 100)
# print(c1.description())
# c1.go(100)
# c1.go(50)
# c1.go(70)
# print(c1.mileage())
# print(c1.desc_battery())


class Battery:
    def __init__(self, bat):
        self.bat = bat

    def desc_battery(self):
        return f'Battery: {self.bat}%'


class ElCar(Car, Battery):
    def __init__(self, company, model, year, bat):
        Car.__init__(self, company, model, year)
        Battery.__init__(self, bat)

    def go(self, km):
        km_pos = self.bat * 2
        if km_pos >= km:
            self.mileage_ += km
            self.bat -= km / 2
            print(f'My {self.company} drove {km} km, battery: {self.bat}%.')
        else:
            self.mileage_ += km_pos
            self.bat = 0
            print(f'My {self.company} drove {km_pos} km, battery: {self.bat}%.')
            print('Battery is low.')


# c1 = ElCar('Tesla', "S", 2020, 100)
# print(c1.description())
# c1.go(100)
# c1.go(50)
# c1.go(70)
# print(c1.mileage())
# print(c1.desc_battery())


class A:
    def aaa(self):
        print("class A. Method aaa()")


class B(A):
    def bbb(self):
        self.aaa()
        print("class B. Method bbb()")


class C(B):
    def ccc(self):
        self.aaa()
        self.bbb()
        print("class C. Method ccc()")


# c = C()
# c.ccc()


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_pr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_pr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# geom = [r1, r2, s1, s2, t1, t2]
#
# for g in geom:
#     print(g.get_pr())


# print(type(1) is int)
# print(type(1) is bool)
# print(type(True) is int)
# print(type(True) is bool)
# print()
#
# print(isinstance(1, int))
# print(isinstance(1, bool))
# print(isinstance(True, int))
# print(isinstance(True, bool))


# from abc import ABC, abstractmethod
#
#
# class Goods(ABC):
#
#     @abstractmethod
#     def sell(self):
#         ...
#
#
# class Apple(Goods):
#     def sell(self):
#         print('Hello')
#
#
# ap = Apple()
# ap.sell()

