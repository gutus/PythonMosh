status_kirim = str(
    input("Status apakah sudah terkirim? (True/False)"))  # User harus menginputkan kata true untuk value True

# Untuk memastikan bahwa semua yg diketikkan user dirubah ke format lowercase dengan menggunakan fungsi .lower()
status_kirim = status_kirim.lower()
for number in range(1, 4):  # Dicoba selama 3 kali
    print("Pengiriman", number * ".", number)
    if status_kirim == "true":  # Trigger valid akan dicompare dan harus sama persis dengan string "true", selain ini akan break dan dilempar ke Else
        print("Terkirim sukses!")
        break
else:
    print(f"Sudah dicoba sebanyak {number} kali dan masih belum terkirim.")
