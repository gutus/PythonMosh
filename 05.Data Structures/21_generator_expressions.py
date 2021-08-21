# Genrerator Expression
# Pokona mah kitu cenah jang menghemat penggunaan memory dina aplikasi nu intens ngitung angka gede teuing
from sys import getsizeof

values = (x*2 for x in range(10))
# Untuk ngecek sebagai apakah variabel values di atas, list ataukah generator object?
print(values)
# mengukur seberapa besar memory yg diambil untuk menyimpan data variabel values
print("gen values:", getsizeof(values))
for x in values:
    print(x)

# Untuk membandingkan besar memory yg digunakan untuk iterabale item hingga 1000000 dibandingkan variabel Values
values2 = (y*2 for y in range(100))
print("gen values 2:", getsizeof(values2))
for y in values2:
    print(y)

# Dalam bentuk list, memory yg digunakan jauh lebih besar dibandingkan dalam bentuk generator object
values3 = [z*2 for z in range(100)]
print("list values 3:", getsizeof(values3))
for z in values3:
    print(z)
