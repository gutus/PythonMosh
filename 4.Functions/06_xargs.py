# XARGS
# Sample 1 Fungsi Perkalian dari Argumen pada Fungsi multiply(x,y,z,a)
def multiply(*numbers):
    total = 1  # variabel total yg akan diiterabel diinisiasi dengan nilai awal 1
    for number in numbers:
        total *= number  # Untuk menghasilkan perkalian total = total * number
    return total  # Untuk menghasilkan output dari total


print("XARGS untuk fungsi penjumlahan multiply(2,3,4,5)")
print(multiply(2, 3, 4, 5))  # Akan menghasilkan perkalian 2*3*4*5 = 120
print("XARGS untuk fungsi penjumlahan multiply(3,4,5,6,7)")
print(multiply(3, 4, 5, 6, 7))  # Akan menghasilkan perkalian 3*4*5*6*7 = 2520

# Sample 2 Fungsi Penjumlahan dari Argumen pada Fungsi addition(x,y,z,a)


def addition(*numbers):
    total = 0  # variabel total yg akan diiterabel diinisiasi dengan nilai awal 0, karena ini penjumlahan, beda dengan perkalian
    for number in numbers:
        total += number  # Untuk menghasilkan perkalian total = total + number
    return total  # Untuk menghasilkan output dari total


print("XARGS untuk fungsi penjumlahan addition(2,3,4,5)")
print(addition(2, 3, 4, 5))  # Akan menghasilkan penjumlahan 2+3+4+5 = 14
print("XARGS untuk fungsi penjumlahan addition(3,4,5,6,7)")
print(addition(3, 4, 5, 6, 7))  # Akan menghasilkan penjumlahan 3+4+5+6+7 = 25
print("\n\n")
# Sample 3 Fungsi Iterable dari Argumen pada Fungsi daftar(x,y,z,a)

print("Sample 3 Iterable deret angka dengan xargs >>> daftar(2,3,4,5,6,7)")
def daftar(*angka):
    for bilangan in angka:
        print(bilangan)
daftar(2,3,4,5,6,7)
