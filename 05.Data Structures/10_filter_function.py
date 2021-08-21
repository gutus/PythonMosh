# FILTER FUNCTION

items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 2),
    ("Product1", 12),
]

x = filter(lambda item: item[1] >= 10, items)
print(x)

print("Merubah filter object menjadi list dengan filter harga >= 10")

filtered_list = list(filter(lambda item: item[1] >= 10, items))
print(filtered_list)
