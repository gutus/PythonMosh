# WORKING WITH DIRECTORIES
# Penjelesan detail fitur dan penggunaan ada di link ini http://etcode.com/python/pathlib/


from pathlib import Path

# print(Path.cwd())
path = Path("ecommerce")
# print(path.exists()) #perintah untuk memeriksa apakah path dengan nama string itu ada
# path.mkdir()  # perintah membuat direktori mkdir dengan nama direktori sesuai variable path
# path = Path.cwd() / "my_new_made_folder"
# path.mkdir()

# path = Path.cwd() / "new_sub_folder"
# path.mkdir()
# print(path.cwd())
# path.rmdir()  # perintah menghapus direktori rmdir dengan nama direktori sesuai variable path
# path.rename("ecommerce_ke_dua") # perintah merubah nama direktori rename dengan nama direktori sesuai string yg nama yg naru

# for p in path.iterdir():
#   print(p)
path_array = [p for p in path.iterdir() if p.is_dir()]
print(
    f"Untuk menampilkan direktori menggunakan p for p in path.iterdir() if p.is_dir()\n\n {path_array}")
print("\nUntuk memunculkan file jenis .PY menggunakan fungsi berikut p for p in path.glob(\"*.py\") ")
file_py = [p for p in path.glob("*.py")]
print(file_py)
print("\nUntuk memunculkan file jenis .TXT menggunakan fungsi berikut p for p in path.glob(\"*.txt\") ")
file_txt = [p for p in path.glob("*.txt")]
print(file_txt)
print("\nUntuk memunculkan semua jenis file menggunakan fungsi berikut p for p in path.glob(\"*.*\") ")
file_all = [p for p in path.glob("*.*")]
print(file_all)
