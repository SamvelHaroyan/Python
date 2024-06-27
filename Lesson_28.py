# # 3 hat metodner kan (class, static)
# class Anun:
#     sides = 3  # classi atribut
#
#     # CALSS method
#     @classmethod
#     def info(cls):
#         return f"this is text {cls.sides}"
#
#     # static method
#     @staticmethod
#     def text():
#         return "this is a text"
#
#
# firstAnun = Anun()
# print(Anun.info())  # aranc obyekti kanchecinq functian
# print(firstAnun.info())
#
#
# print(Anun.text())


class Vector:
    min_coord = 0
    max_coord = 100

    @classmethod
    def validate(cls, a):
        return cls.min_coord < a < cls.max_coord

    def __init__(self, x, y):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            raise ValueError("Invalid Error")

    @staticmethod
    def lenght(a, b):
        return (a ** 2 + b ** 2) ** 0.5

    def get_coord(self):
        return f"({self.x}, {self.y}), lenght = {self.lenght(self.x, self.y)}"

    @staticmethod
    def operation(vect1, vect2, op="+"):
        """
        op: +, -, *
        """
        if op == "+":
            return Vector(vect1.x + vect2.x, vect1.y + vect2.y)  # stexcecinq nor obyekt Vectorov ev stacanq nor vektor
        elif op == "-":
            return Vector(vect1.x - vect2.x, vect1.y - vect2.y)
        elif op == "*":
            return vect1.x * vect2.x + vect1.y * vect2.y


# v1 = Vector(4, 5)
# v2 = Vector(2, 3)
# v3 = Vector.operation(v1, v2, "+")
# v4 = Vector.operation(v1, v2, "-")
# s1 = Vector.operation(v1, v2, "*")
# print("Vector 1:", v1.get_coord())
# print("Vector 2:", v2.get_coord())
# print("Vector 3:", v3.get_coord())
# print("Vector 4:", v4.get_coord())
# print("Scaliar multipliction:", s1)


#####################################################


# ENCAPSULATION  nra hamar e vor classi meji atributnery hasaneli linen menak classi mej
# public, protected, private
class Vector1:
    min_coord = 0
    max_coord = 100

    @classmethod
    def __validate(cls, a):  # private method
        return cls.min_coord < a < cls.max_coord

    def __init__(self, x, y):
        if self.__validate(x) and self.__validate(y):
            self._x = x  # protected
            self.__y = y  # private
        else:
            raise ValueError("Invalid Error")

    @staticmethod
    def length(a, b):
        return (a ** 2 + b ** 2) ** 0.5

    def get_coord(self):
        return f"({self._x}, {self.__y}), length = {self.length(self._x, self.__y)}"

    @staticmethod
    def operation(vect1, vect2, op="+"):
        """
        op: +, -, *
        """
        if op == "+":
            return Vector1(vect1._x + vect2._x, vect1._Vector1__y + vect2._Vector1__y)
        elif op == "-":
            return Vector1(vect1._x - vect2._x, vect1._Vector1__y - vect2._Vector1__y)
        elif op == "*":
            return vect1._x * vect2._x + vect1._Vector1__y * vect2._Vector1__y
        else:
            raise ValueError("Unsupported operation")

    def __del__(self):
        print("Delete")
        del self


v1 = Vector1(4, 5)
print(v1._x)
print(v1._Vector1__y)  # stacanq private-y classic durs (inqy irakanum protected a)
print(v1.__dict__)

vv1 = Vector1(4, 5)
del vv1  # kranq stex kanchenq u jnjenq obyekty mer

v2 = Vector1(2, 3)
v3 = Vector1.operation(v1, v2, "+")
v4 = Vector1.operation(v1, v2, "-")
s1 = Vector1.operation(v1, v2, "*")  # int tip a dra hamar destructor chexav

print("Vector 1:", v1.get_coord())
print("Vector 2:", v2.get_coord())
print("Vector 3:", v3.get_coord())
print("Vector 4:", v4.get_coord())
print("Scalar multiplication:", s1)
