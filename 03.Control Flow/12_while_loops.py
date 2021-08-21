# WHILE LOOPS
number = int(input("Masukkan angka yg diinginkan >>> "))
print(
    f"1. Bilangan awal yang ditentukan adalah {number}, dan akan dibagi 2 berurut hingga 0")
while number > 0:
    print(number)
    number = number // 2
# Augmented Assignment
number2 = int(input("2. Masukkan angka yg diinginkan >>> "))
print(
    f"2. Bilangan awal yang ditentukan adalah {number2}, dan akan dibagi 2 berurut hingga 0")
while number2 > 0:
    print(number2)
    number2 //= 2  # Menggunakan augmented assignment hasilnya sama dengan number = number // 2

print("Sample ala CLI Command, ketik quit untuk keluar dr program")
# Sample 3 Command dengan while
# Simulasi program CLI yang akan quit ketika peintah quit dimasukkan,
# selebihnya akan ECHO command yg dimasukkan
command = ""  # Sebagai container menggunakan string kosong
while command.lower() != "quit":  # menggunakan fungsi lower untuk memastikan semua command yg masuk dievaluasi sebagai lowercase
    command = input(">>>")  # Prompt yg ditampilkan >>>
    # Selama belum terdetek quit, input pada variabel command akan dikeluarkan.
    print("ECHO ", command)
