# DATA CLASS
from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
# Untuk cek ID p1 di memory
print(f"ID memory of p1 >> {id(p1)}")

p2 = Point(10, 2)  # ganti nilai x dan y untuk menguji
print(f"ID memory of p1 >> {id(p2)}")  # Untuk cek ID p2 di memory

print(f"Apakah p1 == p2 >>> {p1 == p2}")

# Versi penyederhanaan dengan mengimpor module
print("\nPenyederhanaan dengan module colections - namedtuple")
# Jangan lupa, argumen ke 2 menggunakan bentuk tuple index x,y, sifatnya imutable karena tuple
Score = namedtuple("Score", ["x", "y"])
p2 = Score(x=2, y=3)
p3 = Score(x=2, y=3)  # Rubah nilai x dan y untuk menguji logic yg kita buat
# cukup dengan 4 baris
print(f"Apakah nilai p2 {p2} == p3 {p3} >>> {p2 == p3}")
print(f"Apakah nilai p2 {p2} > p3 {p3} >>> {p2 > p3}")
print(f"Apakah nilai p2 {p2} < p3 {p3} >>> {p2 < p3}")
