# COST OF RAISING EXCEPTIONS


# Sample Code 1
from timeit import timeit
code1 = """
def calculate_xfactor(age):  # Membuat fungsi umur
    if age <= 0:  # logic yang ingin di detect
        # jenis error yg ingin dinaikkan ValeError
        raise ValueError("Age cannot be 0 or less")
    return 10/age  # rumus untuk menentukan


try:
    calculate_xfactor(-2)
except ValueError as error:
    pass #Untuk mengganti fungsi print screen dan cuma passing code
"""

# Sample Code 2
code2 = """
def calculate_xfactor(age):  # Membuat fungsi umur
    if age <= 0:  # logic yang ingin di detect
        return None  #Tanpa raising error, cukup dengan return None, waktu eksekusi menjadi lebih cepat
    return 10/age  # rumus untuk menentukan


try:
    calculate_xfactor(-2)
except ValueError as error:
    pass #Untuk mengganti fungsi print screen dan cuma passing code
"""

print("Code 1 takes time >>> ", timeit(code1, number=10000))
print("Code 2 takes time >>> ", timeit(code2, number=10000))
