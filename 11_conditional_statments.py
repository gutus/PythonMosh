# CONDITIONAL STATEMENTS
temp = int(input("Temperature sekarang: "))

if temp > 26:
    print("Panas juga ya...")
elif temp >= 35:
    print("Asli panas banget ini!")
else:
    print("Udaranya terasa dingin ya...")

# Ketika temperature terdeteksi lebih dari 26 program akan langsung eksekusi logic if pertama
# elif seolah akan terabaikan, untuk itu bisa diperbaiki dengan memperbaiki urutannya

temp2 = int(input("Temperature sekarang berapa?  "))

if temp2 > 35:
    print("Asli panas banget ini!")
elif temp2 > 26:
    print("Panas juga ya...")
else:
    print("Udaranya terasa dingin ya...")

# Berikan masing-masing termperature pada angka 27 dan 37,
# perhatikan perbedaan respon kedua program terhadap nilai variabel yg sama sekalipun.
