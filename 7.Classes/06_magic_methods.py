# MAGIC METHODS
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # Sample magic method, googling keyword magic method n python
        return f"{self.x}, {self.y}"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(f"Nilai point sebelumnya {point}.")
print(f"Nilai point setelah diconvert menjadi string  {str(point)}.")
