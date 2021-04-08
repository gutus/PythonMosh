# TERNARY OPERATORS
usia = int(input("Berapakah usia anda: "))

if usia >= 24:
    print("Anda dapat mengajukan kredit pembelian.")
else:
    print("Anda belum cukup usia untuk mengajukan kredit pembelian.")

# Menggunakan logika yg sama kita bisa buat program yg lebih ringkas

umur = int(input("Berapakah usia anda sekarang?"))
message = "Anda berhak mengajukan kredit pembelian" if umur >= 28 else "Anda belum berhak mengajukan kredit pembelian."
print(message)

# Menggunakan ternary operators ini hanya memerlukan 3 komponen, variabel, message dan print untuk message
# Logic disematkan di message
