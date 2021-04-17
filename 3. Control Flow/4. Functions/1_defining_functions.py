# DEFINING FUCNTIONS
def greet():
    print("Hi there ")
    print("Welcome aboard")


greet()  # Untuk memanggil function yg telah dibuat cukup dengan menulis nama function()

print("Sample Function dengan megambil data user input")
nama = str(input("Salam, boleh saya tahu nama anda? \n"))
gender = str(input("Apa jenis kelamin anda? (L/P) \n"))
usia = int(input("Berapa usia anda saat ini? \n"))
keluhan = str(input("Apa keluhan yg anda rasakan? \n"))
if gender.lower() == "l" and usia > 35:
    gender = "Pak"
elif  gender.lower() == "p" and usia > 35:
    gender = "Bu"
else:
    gender = ""
def salam():
    print(f"Salam kenal {gender} {nama}")
    print(f"Di usia {gender} {nama} yang menginjak {usia} tahun ini")
    print(f"{gender} {nama} harus lebih banyak istirahat, menghindari stres dan menjaga asupan gizi")
    print(f"Keluhan {gender} {nama} mengenai {keluhan} akan kami sampaikan kepada Dokter anda")
    print(f"Terimakasih telah menggunakan jasa klinik ini, \n Semoga {gender} {nama} lekas sembuh. ")

salam()