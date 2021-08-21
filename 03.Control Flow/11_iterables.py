# ITERABLES = Objek yang dapat diakses melalui perulangan
string = "ini adalah string"
list = ["ini", "adalah", "list"]
tuple = ("ini", "adalah", "tuple")
dictionary = {"ini": 1, "adalah": 2, "dictionary": 3}
set = set(["ini", "adalah", "set"])
frozenset = frozenset(["ini", "adalah", "frozenset"])

print("Iterabale String >>> string = \"ini adalah string\"")
for char in string:  # Mengakses tiap karakter dari objek string
    print(char)

print("\n")
print("Iterabale List >>> list = [\"ini\", \"adalah\", \"list\"]")
for word in list:  # Mengakses tiap kaata dari objek list
    print(word)

print("\n")
print("Iterabale Tuple >>> tuple = (\"ini\", \"adalah\", \"tuple\")")
for word2 in tuple:  # Mengakses tiap kaata dari objek list
    print(word2)

print("\n")
print(
    "Iterabale Dictionary >>> dictionary = {\"ini\": 1, \"adalah\": 2, \"dictionary\": 3}")
for keyword in dictionary:  # Mengakses tiap kaata dari objek list
    print(keyword)
