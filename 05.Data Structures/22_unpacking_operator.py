# Unpack Operator List
# Digunakan untuk membongkar value iterable, * untuk tiap 1 value, ** untuk unpack dictionary
from sys import getsizeof
# Unpack Operator List
numbers = [1, 2, 3, 4, 5]  # Contoh list numbers
print(f"Dengan print list variabel biasa print(numbers) >>> {numbers}")
print("Menggunakan unpack operator * dengan print(*numbers)>>>", *numbers)
print("Besar memory untuk variabel list numbers >>>", getsizeof(numbers))
print("\n " * 3)
# Unpcak Operator Tupple
numbers2 = (1, 2, 3, 4, 5)  # Contoh list numbers
print(f"Dengan print variabel tupple biasa print(numbers) >>> {numbers2}")
print("Menggunakan unpack operatr * dengan print(*numbers)>>>", *numbers2)
print("Besar memory untuk variabel tupple numbers >>>", getsizeof(
    numbers2))  # besar memory yg digunakan tupple lebih kecil
print("\n " * 3)
# Unpcak Operator List Range
value1 = list(range(5))  # Contoh list numbers
print(f"Dengan print variabel tupple biasa print(numbers) >>> {value1}")
print("Menggunakan unpack operatr * dengan print(*numbers)>>>", *value1)
print("Besar memory untuk variabel tupple numbers >>>", getsizeof(
    value1))
print("\n " * 3)
# Unpcak Operator List Combinations
value1 = [1, 2, 3]
value2 = [6, 7, 9]
value3 = ["a", "b", "c"]
value4 = "Hello"
combine = [*value1, *value2, *value3, *value4]
print(
    f"Dengan print variabel list berikut >>> {value1} \n{value2}\n{value3}\n{value4}")
print("Menggunakan unpack operatr * dengan print(combine)>>>", combine)
print("Besar memory untuk variabel tupple numbers >>>", getsizeof(
    combine))
print(*"Hello")
print("\n " * 3)

# Unpcak Operator Dictionary Combinations
Dictionary1 = {"x": 1}
Dictionary2 = {"y": 2}
Dictionary3 = {"x": 3, "a": 4}
combine1 = {**Dictionary1, **Dictionary2}
combine2 = {**Dictionary1, **Dictionary2, **Dictionary3}
print("Dictionary1", Dictionary1)
print("Dictionary2", Dictionary2)
print("Dictionary3", Dictionary3)
print(f"Print combine1 = (**Dictionary1, **Dictionary2) >>{combine1}")

print("Pada kombinasi dictionary dengan unpack value variabel terakhir yg digunakan sebagai value update")
print(
    f"Print combine2 = (**Dictionary1, **Dictionary2, **Dictionary3) >>{combine2}")
# Perhatikan x: 1 diganti menjadi x: 3 karena sudah diupdate dengan pair x: 3 milik Dictionary 3
print("\n " * 3)
