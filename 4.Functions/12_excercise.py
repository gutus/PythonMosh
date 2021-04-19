# EXCERCISE
# Jika angka yg diinputkan user dapat habis dibagi 3 print string Fizz
# Jika angka yg diinputkan user dapat habis dibagi 5 print string Buzz
# Jika angka yg diinputkan user dapat habis dibagi 3 dan 5 print string FizzBuzz
# Jika angka yg diinputkan user tidak dapat habis dibagi 3 atau 5 print sesuai dengan yg diinput user.
number = int(input("Ketikkan angka yg anda pilih \n"))

print("\n|Jika angka yg diinput bisa dibagi 3 output Fizz;| \n|bisa dibagi 5 Buzz; bisa dibagi 3 dan 5 FizzBuzz;| \n|jika tidak bisa dibagi 3 dan 5 makan output sesuai angka yg diinput|")
print("\n\nOutput yg ditampilkan  ")


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print(">>> FizzBuzz")
    elif number % 5 == 0:
        print(">>> Buzz")
    elif number % 3 == 0:
        print(">>> Fizz")
    else:
        print(f">>>{number}<<< karena bukan kelipatan 3 dan atau 5")


fizzbuzz(number)
