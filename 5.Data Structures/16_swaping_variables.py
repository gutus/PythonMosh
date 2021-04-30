master\x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)
print("z", z)

# Dengan cara yg sama kita bisa membuat nya dengan melakukan positioning assignment

a = 10
b = 11
print (f"Nilai a sebelum di-swap adalah {a}, dan nilai b awalnya {b}.")
a, b = 11, 10
print("Setelah diswap nilai a menjadi b dan nilai b menjadi a maka:")
print(f"Nilai a saat ini adalah {a} dan nilai b menjadi {b}")