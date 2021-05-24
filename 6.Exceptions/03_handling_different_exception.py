# HANDLING DIFFERENT EXCEPTION
try:
    age = int(input("Berapa usia anda saat ini?  "))
    xfactor = 10 / age
except ValueError:  # Digunakan untuk mendeteksi kesalahan, misal jika user memasukkan input selain integer
    print('Usia yang anda masukkan tidak valid')
except ZeroDivisionError:  # dengan bantuan variabel xfactor bisa digunakan untuk mentrigger ZeroDivisionError
    print(f'Usia yang anda masukkan saat ini {age} tidak valid')
else:
    print("Usia yang anda masukkan sudah tepat")
    print(f"Usia anda saat ini {age} tahun.")

# Karena ada dua exception, maka bisa digabung dengan dipisahkan koma
try:
    age2 = int(input("Berapa usia anda saat ini?  "))
    xfactor2 = 10 / age2
except (ValueError, ZeroDivisionError):  # Exception error yg digabung
    print(f"Usia yang anda masukkan tidak valid")
else:
    print("Usia yang anda masukkan sudah tepat")
    print(f"Usia anda saat ini {age2} tahun.")
