# Menuliskan Range Angka Genap dan Menuliskan Jumlahnya
print("Sample Range Angka Genap dari 1 Hingga 10 \n ********* ")
count = 0  # Untuk fungsi penghitung jumlah iterable object
for number in range(1, 10):
    if number % 2 == 0:  # Fungsi modulus untuk mendeteksi bilangan genap, int % 2 = 0 berarti genap, int % 2 = 1 berarti ganjil
        print(f"Angka genap {count+1} >>> {number}")
        count += 1  # Setiap angka genap tercatat count akan bertambah 1
print()
print(f"Kita punya  {count} angka genap.")
print(" \n \n")
print("Sample Range Angka Ganjil  1 Hingga 10  \n ********* ")
# Menuliskan Range Angka Genap dan Menuliskan Jumlahnya
count = 0  # Untuk fungsi penghitung jumlah iterable object
for number in range(1, 10):
    if number % 2 == 1:  # Fungsi modulus untuk mendeteksi bilangan ganjil, int % 2 = 1 berarti ganjil, int % 2 = 0 berarti genap
        print(f"Angka genap {count+1} >>> {number}")
        count += 1  # Setiap angka ganjil tercatat count akan bertambah 1
print()
print(f"Kita punya  {count} angka ganjil.")
