# MAGIC METHODS
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x == other.x and self.y == other.y

# def __str__(self):  # Sample magic method, googling keyword magic method n python
# return f"{self.x}, {self.y}"


point = Point(1, 2)
other = Point(1, 2)
print(point == other)
point = Point(5, 5)
other = Point(1, 2)
print(point > other)
