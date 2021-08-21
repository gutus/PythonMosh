print("Sampel for loop pertama - for number in range(3):")
# Sample pertama menggunakan range(1 argumen)
for number in range(3):
    print("1 Mengirim pesan...", number + 1, (number + 1) * ".")
    
print("\nSampel for loop ke dua - for number2 in range(1, 4):")
# Sample ke dua dengan range(start, finish-1) akan menghasilkan output yg sama
for number2 in range(1, 4):
    print("2 Mengirim pesan...", number2, (number2) * ".")

print("\nSampel for loop ke tiga dengan 3 argumen, yg menampilkan angka ganjil - for number3 in range(1, 10, 2):")
# Sample ke dua dengan range(start, finish-1, kelipatan) akan menghasilkan output urutan ganjil
for number3 in range(1, 10, 2):
    print("3 Mengirim pesan...", number3, (number3) * ".")

print("\nSampel for loop ke empat dengan 3 argumen, yg menampilkan angka genap - for number4 in range(2, 10, 2):")
# Sample ke dua dengan range(start, finish-1, kelipatan) akan menghasilkan output urutan ganjil
for number4 in range(2, 10, 2):
    print("4 Mengirim pesan...", number4, (number4) * ".")
