# INHERITANCE
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal, Fish = Child, Sub, Inherit value from Mamama


class Mammal(Animal):
    def walks(self):
        print("walk")


class Fish(Animal):
    def wswim(self):
        print("swim")


sapi = Mammal()
sapi.eat()
print(sapi.age)
