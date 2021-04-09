# LOGICAL OPERATORS
# Ada 3 operator yg dapat dimanfaatkan yaitu and, or dan not
# Contoh pengajuan kredit

# Variabel input pendapatan_tinggi dikonversi menjadi Boolean (True/False)
pendapatan_tinggi = bool(input("Apakah pendapatan anda tinggi? (True/False)"))
# Dikonversi menjadi Boolean agar operator tidak sembarangan memasukkan nilai variabel.
score_credit = bool(input("Apakah score credit anda baik? (True/False)"))
# CASE1
print("CASE 1")
if pendapatan_tinggi and score_credit:  # setiap variabel yg diuji di sini diasumsikan bernilai True
    print("[CASE1]Selamat! Anda dapat mengajukan kredit.")
else:
    print("[CASE1]Maaf! Anda belum dapat mengajukan kredit.")
print("\n" * 2)
print("CASE 2")
message = "[CASE2]Selamat! Anda dapat mengajukan kredit." if pendapatan_tinggi or score_credit else "[CASE2]Maaf! Anda belum dapat mengajukan kredit."
print(message)
# Pada case ke dua, cukup satu variabel bernilai True maka output akan True (Logika Or)
print("\n" * 2)
# Ini skenario pemberian kredit khusu bagi mereka yg score credit nya tidak baik (False)
print("CASE 3")
message = "[CASE3]Selamat! Anda dapat mengajukan kredit." if pendapatan_tinggi and not score_credit else "[CASE3]Maaf! Anda belum dapat mengajukan kredit."
print(message)
# Pada case ke tiga ini, untuk menghasilkan output True variabel pendapatan_tinggi harus True dan variabel score_credit harus False,
# tolong dipahami maksud dr logic ini
