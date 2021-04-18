### DEFAULTS ARGUMENTS
print("Ini adalah contoh pemanggilan fungsi dengan arguments defaults")
print("Misal dengan fungsi increment(number, by=1)")

def increment (number, by=1): #Jika user tidak memasukkan argumen ke dua maka argumen defaults yg diset akan digunakan, dalam hal ini by=1
    return number + by

print(f"Dalam contoh ini kita menambahkan 3 dengan 1 menggunakan default arguments by=1 sehingga didapat ")
print("print(increment(3)) perhatikan pada argumen kedua tidak disuplai nilai, tapi akan tetap menghasilkan: ")
print(increment(3))# Argumen ke dua tidak disuplai, program akan mengambilkan argumen default sebagai gantinya
print("Pada contoh berikut kita suplai argument ke dua, Dalam hal ini print(increment(3, 5)) perhatikan hasilnya,\nargument default akan diabaikan karena user memasukkan argumen ke dua (5). ")
print(increment(3, 5))