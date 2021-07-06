# CONSTRUCTORS
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f"Point ({self.x}, {self.y}, {self.z})")


point = Point(1, 2, 5)
point.draw()
