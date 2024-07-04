# # GETTER SETTER DELETER
#
# class Person:
#     __age_min = 14
#     __age_max = 65
#     __kg_min = 20
#     __passport_val = 11
#
#     def validate_pass(self, a):
#         if isinstance(a, str) and len(a) != self.__passport_val or a[4] != " ":
#             raise ValueError
#         for i in range(len(a)):
#             if i == 4:
#                 continue
#             if not a[i].isdigit():
#                 raise ValueError
#         return True
#
#     def validate_name(self, b):
#         return isinstance(b, list) and len(b) == 3 and all(isinstance(i, str) for i in b)
#         # all ete mejy sax true exav uremn veradarcnum e true
#         # any erb vor gone mi haty true exav uremn true e veradarcnum
#
#     def __init__(self, fullName, age, passport, kg):
#         if self.validate_name(fullName):
#             self.__fullName = fullName
#         if isinstance(age, (int, float)) and self.__age_min <= age <= self.__age_max:
#             self.__age = age
#         else:
#             raise ValueError("Invalid age.")
#         if self.validate_pass(passport):
#             self.__passport = passport
#         if isinstance(kg, (int, float)) and kg >= self.__kg_min:
#             self.__kg = kg
#         else:
#             raise ValueError("Invalid weight.")
#
#     @property
#     def Human(self):
#         return self.__fullName, self.__age, self.__passport, self.__kg
#
#     @Human.setter
#     def Human(self, values):
#         name, age, passport, kg = values
#         if self.validate_name(name):
#             self.__fullName = name
#         else:
#             raise ValueError("Invalid name format.")
#         if isinstance(age, (int, float)) and self.__age_min <= age <= self.__age_max:
#             self.__age = age
#         else:
#             raise ValueError("Invalid age.")
#         if self.validate_pass(passport):
#             self.__passport = passport
#         if isinstance(kg, (int, float)) and kg >= self.__kg_min:
#             self.__kg = kg
#         else:
#             raise ValueError("Invalid weight.")
#
#     @Human.deleter
#     def Human(self):
#         del self.__fullName
#         del self.__age
#         del self.__passport
#         del self.__kg
#
#
# p1 = Person(["Gev", "Smbatyan", "Gexami"], 63, '1234 567890', 83)
# print(p1.Human)
#
# p1.Human = (["Ara", "Petrosyan", "Valodi"], 40, '5678 123456', 75)
# print(p1.Human)
#

