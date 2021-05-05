### XXARGS
def data_user(**user):
    print("Misal jika hanya menggunakan argumen user utuh user() maka hasilnya >>>", user)
    print("Misal jika menggunakan argumen user utuh user([\"name\"]) maka hasilnya >>>", user["name"])
    print("Misal jika menggunakan argumen user id user([\"id\"]) maka hasilnya >>>", user["id"])
    print("Misal jika menggunakan argumen user age user([\"age\"]) maka hasilnya >>>", user["age"])

data_user(id=1, name="Gutus", age=25)