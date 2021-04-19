# DEBUGGING
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print("Start")
print(multiply(1, 2, 3))


print("Setelah debugging, ditemukan error indentasi pada line #6, untuk kemudian indentasi diperbaiki")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Finish")
print(multiply(1, 2, 3))
# print("Finish")
# print(multiply(1, 2, 3))
