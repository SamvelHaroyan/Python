import math


# # ex 1
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def true_triangle(self, a, b, c):
#         return a + b > c and a + c > b and b + c > a
#
#     def get_sides(self):
#         return self.a, self.b, self.c
#
#     def paragic(self):
#         return self.a + self.b + self.c
#
#     def makeres(self):
#         s = self.paragic() / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
#
#     def havasarakoxm(self):
#         return self.a == self.b == self.c
#
#     def havasarasrun(self):
#         return self.a == self.b or self.a == self.c or self.b == self.c
#
#     def ankanon(self):
#         return self.a != self.b and self.a != self.c and self.b != self.c
#
#     def uxxankyun_erankyun(self):
#         a, b, c = self.a, self.b, self.c
#         if a > b and a > c:
#             return a * a == b * b + c * c
#         elif b > a and b > c:
#             return b * b == a * a + c * c
#         else:
#             return c * c == a * a + b * b
#
#     def nergcac_shrjanagic(self):
#         return self.makeres() / (self.paragic() / 2)
#
#     def artagcac_shrjanagic(self):
#         return (self.a * self.b * self.c) / (4 * self.makeres())
#
#
# triangle = Triangle(3, 4, 5)
# print("Sides:", triangle.get_sides())
# print("Paragic:", triangle.paragic())
# print("Makeres:", triangle.makeres())
# print("Havasarakoxm:", triangle.havasarakoxm())
# print("Havasarasrun:", triangle.havasarasrun())
# print("Ankanon:", triangle.ankanon())
# print("Uxxankyun_erankyun:", triangle.uxxankyun_erankyun())
# print("Nergcac_shrjanagic:", triangle.nergcac_shrjanagic())
# print("aArtagcac_shrjanagic:", triangle.artagcac_shrjanagic())


# ex 2
class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.milage = 0

    def description(self):
        return f"{self.company}, {self.model}, {self.year}"

    def mileage(self):
        return f"{self.milage}"

    def go(self, km):
        self.milage += km * 0.621371
        return self.milage


my_car = Car('Chevrolet', 'Impala', 1967)
print(my_car.description())
print(my_car.mileage())
my_car.go(27)
print(my_car.mileage())

