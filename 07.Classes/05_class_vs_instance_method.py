# CLASS Volume Kubik

class Kubik:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.volume = panjang * lebar * tinggi
        return

    # def draw(self):
        #print(f"Panjang {self.panjang}, lebar {self.lebar}, tinggi {self.tinggi} sehingga Volume = {volume}")###


panjang = int(input("Masukkan panjang kotak "))
lebar = int(input("Masukkan lebara kotak "))
tinggi = int(input("Masukkan tinggi kotak "))

kubik = Kubik(panjang, lebar, tinggi)

print(f"Panjang dari kubik >>> {kubik.panjang}")
print(f"Lebar dari kubik >>> {kubik.lebar}")
print(f"Tinggi dari kubik >>> {kubik.tinggi}")
print(
    f"Volume kubik adalah {kubik.panjang} * {kubik.lebar} * {kubik.tinggi} \n Volume kubik >>> {kubik.volume}")
