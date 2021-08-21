from pathlib import Path
# WORKING WITH FILES

import pathlib
# Fungsi Creation Time merubah data ctime byte menjadi user readbale
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
path.exists()
path.stat()  # menampilkan status dari path
# path.rename("ecommerce/namabaru.txt") # merubah nama file menjadi nama yg baru
# path.unlink()  # Untuk menghilangkan file, untuk direktory gunakan rmdir()
print(path.stat())
print("Untuk menyederhanakan dan mengambil info CREATION TIME\n\nKita gunakan fungsi CTIME  ke dalam CTIME print(ctime(path.stat().st_ctime)) ")
print(ctime(path.stat().st_ctime))

# path.read_bytes()  # Untuk membaca file dalam format data byte
# print(path.read_text())
# path.write_text("/nIni sample text tambahan.")
# print(path.read_text())

print("Ini metode lain untuk menyalin satu file ke file lainnya menggunakan ")

source = Path("ecommerce/__init__.py")
target = Path("ecommerce/file_hasil_copy_dari_source__init__.py")

# target.write_text(source.read_text()) #cara manual untuk clone file dengan fungsi write dan read dengan segala keribetan yg ada
# Dengan menggunakan fungsi shutil >>> shelll utility perintah copy lebih sederhana.
shutil.copy(source, target)
print(
    f"Dengan fungsi shutil.copy(source, target) \ntarget.readtext() >>> \t{target.read_text()}")
