###Handling Exceptions
#ketika program tidak dipersiapkan untuk mengeluarkan exception, begitu terdapat error maka proram akan crash

# Sample program 1
try:
    usia =int(input("Berapa usia anda sekarang: "))
    print(f"Saat ini usia anda {usia} tahun.")
except ValueError:
    print("Masukkan nilai berupa angka saja, jangan gunakan huruf.")

print("Program 1 telah selesai dijalankan")

# Sample program 2 dengan detail error
try:
    usia2 =int(input("Berapa usia anda sekarang: "))
    print(f"Saat ini usia anda {usia2} tahun.")
except ValueError as ex:
    print("Masukkan nilai berupa angka saja, jangan gunakan huruf.")
    print(ex)
    print(type(ex))
else: #Line ini akan dieksekusi jika line try: valid
    print("Bagus, anda mengisi dengan tepat, tidak ada error yg terdeteksi")
print("Program 2 telah selesai dijalankan")

