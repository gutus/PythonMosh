# RAISING EXCEPTIONS
def calculate_xfactor(age):  # Membuat fungsi umur
    if age <= 0:  # logic yang ingin di detect
        # jenis error yg ingin dinaikkan ValeError
        raise ValueError("Age cannot be 0 or less")
    return 10/age  # rumus untuk menentukan


try:
    calculate_xfactor(-2)
except ValueError as error:
    print(error)
