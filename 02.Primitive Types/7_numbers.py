#Number in Python
print("Number in Python")
print("\n")
a = 20
b = 3
print(f"Nilai a = {a}, \nNilai b = {b}")
print("\n")
print(f"1. Penjumlahan variabel a+b = {a+b} >>>\tPenjumlahan dua variabel")
print(f"2. Pengurangan variabel a-b = {a-b} >>>\tPengurangan dua variabel")
print(f"3. Perkalian variabel a*b = {a*b} >>>\tPerkalian dua variabel")
print(f"4. Pembagian dengan hasil desimal variabel a/b = {a/b} >>>\tPembagian dua variabel")
print(f"5. Pembagian dengan hasil bulat variabel a//b = {a//b} >>>\tPembagian bulat dua variabel")
print(f"6. Modulus dengan hasil sisa dari hasil pembagian  a%b = {a%b} >>>\n   Pembagian modulus dua variabel a ({a}) dikurangi b ({b}) dikali hasil dari  (a//b) {a//b} tersisalah hasil modulus {a%b}")
print(f"7. Pangkat dengan faktor pengali  a**b = {a**b} >>>\tPangkat dinatara variabel a ({a}) pangkat ({b})dengan hasil  {a**b}")

x = 7
y = 3
print("Augmented Assignment Operator untuk mempersingkat")
print(f"Misal x = x + y bisa disingkat dengan menulisnya x += y, dengan hasil yg akan tetap sama")
print("")
print(f"Nilai x = {x} \t Nilai y = {y}")
z= x+y
print(f"1. Penjumlahan variabel z = x + y dengan hasil  {z} >>>\tPenjumlahan konvensional")
x += y
print(f"2. Penjumlahan variabel dengan augmented assignment  x += y dengan hasil  {x} >>>\tPenjumlahan augmented assignment")
print(f"Karena nilai x telah berubah dengan x = {x} \t Nilai y = {y} maka")
x *= y
print(f"3. Perkalian variabel dengan augmented assignment  x *= y dengan hasil  {x} >>>\tPerkalian augmented assignment")
print(f"Karena nilai x telah berubah dengan x = {x} \t Nilai y = {y} maka")
x /= y
print(f"4. Pembagian variabel dengan augmented assignment  x /= y dengan hasil  {x} >>>\tPembagian augmented assignment")
print(f"Karena nilai x telah berubah dengan x = {x} \t Nilai y = {y} maka")
x //= y
print(f"4. Pembagian variabel dengan augmented assignment  x //= y dengan hasil  {x} >>>\tPembagian augmented assignment")