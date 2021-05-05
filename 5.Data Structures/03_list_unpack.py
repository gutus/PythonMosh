# LIST UNPACK
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, third, *other, last = numbers
print(f"Ini adalah list utuh dari numbers = {numbers}")
print(f"Dengan menggunakan list unpack >>> first, second, third, *other, last = numbers")
print(f"Ini adalah list urutan first>>> {first}")
print(f"Ini adalah list urutan second >>> {second}")
print(f"Ini adalah list urutan third >>> {third}")
print(f"Ini adalah list urutan last >>> {last}")
print(f"Ini adalah list urutan other >>> {other}")
