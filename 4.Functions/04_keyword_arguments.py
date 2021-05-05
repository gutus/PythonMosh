### KEYWORD ARGUMENTS
print("Ini adalah contoh pemanggilan fungsi dengan arguments untuk mempermudah")

def increment (number, by):
    return number + by

print(f"Dalam contoh ini kita menambahkan 3 dengan 1 sehingga didapat ")
print("print(increment(3,1)) dengan hasil: ")
print(increment(3,1))# Tampak kurang informatif
print("Dengan cara yg sama kita bisa menmbahkan keyword pada argument misal dengan menulis nama keyword = argument \nDalam hal ini print(increment(3, by = 1)")
print(increment(3, by=1))