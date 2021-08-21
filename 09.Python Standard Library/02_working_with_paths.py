# WORKING WITH PATHS
from pathlib import Path

Path(r"C:\Program Files\Microsoft")  # Contoh path ke direcory windows
Path("/usr/local/bin")  # Contoh path ke directory python
Path()  # Contoh path ke directory aktif saat ini/current
Path("ecommerce/__init__.py")  # Contoh path ke direcory packages
# Contoh path ke direcory packages menggunakan combine string (concatenate)
Path() / "ecommerce" / "__init__.py"
Path.home()  # Contoh path ke home direcory user saat ini (current user)


# Sample penggunaan
path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()

print(f"Ini adalah path.name >>>{path.name}")
print(f"Ini adalah path.stem >>> {path.stem}")
print(f"Ini adalah path.suffix >>> {path.suffix}")
print(f"Ini adalah path.parrent >>> {path.parent}")
path = path.with_suffix(".txt")

print(
    f"Ini adalah path dengan path.with_suffix(.txt) mengubah .py menjadi .txt >>> {path}")
