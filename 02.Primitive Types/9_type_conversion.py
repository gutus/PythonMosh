x = int(input("Nilai x yang kamu pilih: "))
y = 6

#print(f"Nilai x yang kamu pili:{x} ")
print(f"Nilai y yang sudah ada: {y}")
print(f"1. Jika kedua bilangan ditambahkan, maka {x} + {y} = {x+y}")
print("***" * 3)
print(
    f"2. Jika nilai x dikonversi menjadi string dengan str(x), \n maka nilai x menjadi  {str(x)} dan nilai {y} sehingga ketika digabungkan (concatenate) menjadi {str(x)+str(y)}")
# Skenario Memaksa user untuk input hanya bilangan
a = input("Masukkan nilai a: ")
if a.isdigit():  # memeriksa apakah nilai yg diinput adalah angka
    print(f"Nilai a + y adalah {a} + {y} = {a+Y}")
else:
    print(f"Masukkan nilai a berupa angka!!!")
