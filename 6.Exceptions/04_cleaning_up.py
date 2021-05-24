# CLEANING UP
try:
    file = open("../app.py")
    age2 = int(input("Berapa usia anda saat ini?  "))
    xfactor2 = 10 / age2
except (ValueError, ZeroDivisionError):  # Exception error yg digabung
    print(f"Usia yang anda masukkan tidak valid")
else:
    print("Usia yang anda masukkan sudah tepat")
    print(f"Usia anda saat ini {age2} tahun.")
finally:
    file.close()
