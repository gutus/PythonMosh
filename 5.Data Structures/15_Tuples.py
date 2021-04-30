# TUPLES
# Tuples = Read only list, bisa digunakan untuk menyimpan nilai koefisien misal
# Diandai dengan koma dan ()
point = (1, 2)
print(f"List Point dengan nilai (1,2) >>> ", point)
print(type(point))  # Untuk mengecek type data dari variable point

# Tuples juga bisa dikenakan operasi matematik
# Perkalian
point2 = point * 3
print(f"List point (1,2) * 3 menjadi >>> ", point2)
# Penjumlahan
point3 = point2 + (3, 4)
print(f"Penjumlahan point2 + (3,4) menjadi >>>> ", point3)
