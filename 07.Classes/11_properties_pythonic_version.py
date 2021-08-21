# Properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative!")
        self.__price = value


product = Product(50)
product.price = 23  # atribut properties sudah masuk, cukup dengan call setelah prodcut
print(product.price)