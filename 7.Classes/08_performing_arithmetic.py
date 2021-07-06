
# PERFORMING ARITHMETIC OPERATIONS
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Operasi penjumlahan
        return self.x + other.x and self.y + other.y

    def __sub__(self, other):  # Operasi pengurangan
        return self.x - other.x and self.y - other.y

    def __mul__(self, other):  # Operasi perkalian
        return self.x * other.x and self.y * other.y


# def __str__(self):  # Sample magic method, googling keyword magic method n python
# return f"{self.x}, {self.y}"


point = Point(1, 2)
other = Point(1, 2)
point = point
other = other
penjumlahan = point + other
print(f"Penjumlahan dari {point} + {other} = {penjumlahan}")
point = Point(5, 5)
other = Point(1, 2)
pengurangan = point - other
print(f"Pengurangan dari {point} - {other} = {pengurangan}")
perkalian = point * other
print(f"Perkalian dari {point} * {other} = {perkalian}")
