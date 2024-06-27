# oop
# popoxakannery havasar en atributner classeri mej
# functionnnery classum metodner en
class Person:
    hands = 2
    legs = 2

    # constructor
    def __init__(self, name, lastName, age):  # magic methods
        self.name = name
        self.lastName = lastName
        self.age = age

    def run(self, m):  # instance method
        return f"{self.name} runs {m} meter."

    def __str__(self):  # nra hamar e vor aranc functionu kanchelu karoxananq kanchenq iran prosty grelov print("obyekti anuny")
        return f"{self.name} {self.lastName}"


p1 = Person("Avet", "Xachatryan", 20)
p2 = Person("Gexam", "Bazinyan", 80)
print(p1.run(10))
print(p1.legs)
print(p1.age)
Person.hands = 4  # poxec handsy bolori mot
print(p1)
print(p2)
