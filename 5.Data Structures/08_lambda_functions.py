# LAMBDA FUNCTIONS
items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 2),
    ("Product1", 12),
]


items.sort(key=lambda item: item[1])
print(items)
