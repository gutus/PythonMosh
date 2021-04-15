usia = int(input("Berapa usia anda?  "))

if usia >= 18 and usia <= 35:
    print("1. Anda berhak mengajukan pembiayaan.")
else:
    print("1. Maaf pengajuan anda ditolak.")

### Untuk menyederhanakan logic yg dibuat, dapat digunakan metode chaining seperti berikut
usia2 = int(input("Berapa usia anda?  "))

if 18 <= usia2 <= 35:
    print("2. Anda berhak mengajukan pembiayaan.")
else:
    print("2. Maaf pengajuan anda ditolak.")