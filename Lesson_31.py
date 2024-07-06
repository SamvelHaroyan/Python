# dundle (double underscore) magic methods
# STR


# class Car:
#     def __init__(self, model, year):
#         self.year = year
#         self.model = model
#
#     def __str__(self):
#         return f"{self.model}"
#
#     def __repr__(self):
#         return f"{self.model}, {self.year}"
#
#
# c = Car("Lexus", 2020)
# print(c)
# print(str(c))
# print(repr(c))


class Clock:
    def __init__(self, seconds):
        self.seconds = seconds % 86400

    def __str__(self):
        hours = self.seconds // 3600
        minutes_temp = self.seconds % 3600
        minutes = minutes_temp // 60
        seconds = self.seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __add__(self, other):
        return Clock(self.seconds + other.seconds)



c1 = Clock(3661)
c2 = Clock(3661)
print(c1)
print(c2)
print(c1 + c2)

# print("330".zfill(5))  # 00330
