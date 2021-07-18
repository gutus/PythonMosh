# THE DIR FUNCTION
from ecommerce.shopping import sales

# Untuk menapilkan semua package default yg ada pada directory sales
print(dir(sales))
print(sales.__name__)  # Menampilkan nama packages
print(sales.__package__)  # Menampilkan packages
print(sales.__file__)  # Menampilkan path dari packages sales pada directory.
