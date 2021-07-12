# Method Overriding
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal, Fish = Child, Sub, Inherit value from Mamama


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walks(self):
        print("walk")


class Fish(Animal):
    def wswim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
