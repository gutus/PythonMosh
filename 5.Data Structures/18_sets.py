# SET
# Set adalah kumpulan item yg tidak tersusun, tiap elemen set adalah unik, tidak ada elemen yg ganda
awal = [1, 2, 2, 3, 4, 5]
print(f"Nilai variabel awal adalah {awal}")
satu = set(awal)
print(
    f"Variabel awal dirubah menjadi variabel satu dengan menuliskan >> satu = set(awal) sehingga \nsekarang nilai satu adalah {satu}")
dua = {3, 5, 7}
print(f"Ditambahkan nilai dua = {dua}")
print(f"\nKetika kita gunakan operator OR dengan print(satu | dua)")
print(satu | dua)
print(f"\nKetika kita gunakan operator AND dengan print(satu & dua) \nyg ditampilkan hanya bilangan yg ada pada variabel satu dan dua")
print(satu & dua)
print(f"\nKetika kita gunakan operator DIFFERENT dengan print(satu - dua) \nyg ditampilkan hanya bilangan elemen satu yang tidak ada pada elemen dua")
print(satu - dua)
print(f"\nKetika kita gunakan operator DIFFERENT dengan print(dua - satu) \nyg ditampilkan hanya bilangan elemen dua yang tidak ada pada elemen satu")
print(dua - satu)
print(f"\nKetika kita gunakan operator SYMETRIC DIFFERENT dengan print(dua ^ satu) \nyg ditampilkan hanya bilangan yang tidak ada di antara salah satunya \ntapi tidak pada keduanya, bingung khan?")
print(dua ^ satu)
print(f"\nKetika kita gunakan operator SYMETRIC DIFFERENT dengan print(satu ^ dua) \nyg ditampilkan hanya bilangan yang tidak ada di antara salah satunya \ntapi tidak pada keduanya, bingung khan?")
print(satu ^ dua)
