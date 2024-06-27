import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def true_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def get_sides(self):
        return self.a, self.b, self.c

    def paragic(self):
        return self.a + self.b + self.c

    def makeres(self):
        s = self.paragic() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def havasarakoxm(self):
        return self.a == self.b == self.c

    def havasarasrun(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

    def ankanon(self):
        return self.a != self.b and self.a != self.c and self.b != self.c

    def uxxankyun_erankyun(self):
        a, b, c = self.a, self.b, self.c
        if a > b and a > c:
            return a * a == b * b + c * c
        elif b > a and b > c:
            return b * b == a * a + c * c
        else:
            return c * c == a * a + b * b

    def nergcac_shrjanagic(self):
        return self.makeres() / (self.paragic() / 2)

    def artagcac_shrjanagic(self):
        return (self.a * self.b * self.c) / (4 * self.makeres())


triangle = Triangle(3, 4, 5)
print("Sides:", triangle.get_sides())
print("Paragic:", triangle.paragic())
print("Makeres:", triangle.makeres())
print("Havasarakoxm:", triangle.havasarakoxm())
print("Havasarasrun:", triangle.havasarasrun())
print("Ankanon:", triangle.ankanon())
print("Uxxankyun_erankyun:", triangle.uxxankyun_erankyun())
print("Nergcac_shrjanagic:", triangle.nergcac_shrjanagic())
print("aArtagcac_shrjanagic:", triangle.artagcac_shrjanagic())
