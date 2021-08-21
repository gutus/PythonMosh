# SCOPE
# Local & Global Variabel

# Global Variabel yg bisa diakses dan dipergunakan ulang di fungsi-fungsi yg lain
print("Fungsi Scope Variabel Local dan Global ")
message = " Ini variabel global message dengan isi string = \"A\""


def greet(name):
    message = "Ini variabel local message di dalam fungsi greet() dengan isi string = \"B\""
    print(message)


greet("Gutus")
print(message)
