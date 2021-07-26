# WORKING WITH ZIP FILES
from pathlib import Path
from zipfile import ZipFile

# Untuk zip iterable file pada folder
# with ZipFile("file.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# Untuk ekstrak nama file  pada zip file
with ZipFile("file.zip") as zip:
    print(zip.namelist())  # Print nama file dalam bentuk list
    info = zip.getinfo("ecommerce/__init__.py")
    # Print file size dari file get info __init__.py.
    print(info.file_size)
    print(info.compress_size)
    # Mengekstrak semua file ke folder baru hasil extract
    zip.extractall("hasil_extract")
