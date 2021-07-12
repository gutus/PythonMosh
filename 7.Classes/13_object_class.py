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


m = Mammal()
f = Fish()
# isinstance >>> Apakah m adalah bagian dari instance Animal
print(isinstance(m, Animal))
# isinstance >>> Apakah m adalah bagian dari instance Mammal
print(isinstance(m, Mammal))
# issubclass >>> Apakah Fish adalah bagian dari subclass Animal
print(issubclass(Fish, Animal))
# issubclass >>> Apakah Fish adalah bagian dari subclass Mammal
print(issubclass(Fish, Mammal))
