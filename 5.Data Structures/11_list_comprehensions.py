# LIST COMPREHENSIONS

items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 2),
    ("Product1", 12),
]


print("Merubah filter object menjadi list dengan filter harga >= 10")

prices = list(map(lambda item: item[1], items))
prices = [items[1] for otem in items]
print(prices)
filtered = list(filter(lambda item: item[1] >= 10, items))
