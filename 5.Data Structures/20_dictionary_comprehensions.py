#Dictionary Comprehensions
#Metode tradisional untuk membuat pasangan key: value
print("Menggunakan metode dictionary iterable tradisional")

values= {}
for x in range(5):
    values[x] = x * 2 #Membuat dictionary x: x*2 menggunakan iterable
print(values)

#Metode Dictionary Comprehensions
print("Menggunakan metode dictionary comprehension values2 = {\tx: x*2 for x in range(5)\t}")
values2 = {x: x*2 for x in range(5)} #Straight forward, langsung key: pair dengan value x diambilkan dari iterable
print(values2) #Hasilnya sama dengan iterable dictionary tradisional