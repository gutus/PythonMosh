# Whats is your name
first = str(input("What is your first name? "))
mid = str(input("What is your middle name? "))
last = str(input("What is your last name? "))
name = first + " " + mid[0]+" "+last

print(f"So your name is:  {name} right?")
print(f"Your initial middle name of your {mid} is {mid[0]} right?")
print(f"For simplification may I call you {first[1:].upper()}, Bud? ")
