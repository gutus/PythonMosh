# TYPES OF FUNCTIONS

def greet(name):
    print(f"Hi {name}")


greet("Gutus")

print("Tipe fungsi lainnya dengan menghasilkan output berupa variabel")
# Contoh di bawah ini sampel print biasa dan print ke dalam file content.txt, canggih bener.


def salam(name):
    return f"Hi {name}"


# Tulis argumen di sini, dan cek hasil penulisan di file content.txt
message = salam("Gutus Nirwanto yg ganteng tajir melintir level global")

print(message)  # Perintah sederhana print di terminal
# Perintah membuka file content.txt dengan type writeable (menulis file, tidak hanya membacanya saja) dan di assign ke varibel tulisan.
tulisan = open("4.Function_type_content.txt", "w")
# Fungsi open file writeable yg disembunyikan ke dalam variabel tulisan.  Sehingga di kode selanjutnya cukup memanggil variabel tulisan saja untuk fungsi penulisan.  Panjang bener oenjabarannya :)
# Memerintahkan penulisan variabel message terhadap variabel tulisan pada file sebelumnya
tulisan.write(message)
