# SORTING LISTS
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers)
sorted(numbers)
print(sorted(numbers, reverse=True))
print(sorted(numbers, reverse=False))
print(numbers)
print("\n*" * 3)
items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 2),
    ("Product1", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
