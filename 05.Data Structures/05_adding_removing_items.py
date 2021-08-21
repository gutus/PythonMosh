### ADDING OR REMOVING ITEMS
letter = ["a", "b", "c"]
print(f"Awalnya list letter berisi {letter}")

#Menambahkan items
letter.append("d") # Menambahkan karakter "s" di ujung list
letter.insert(0, "-") # Menambahkan pada index 0 karakter string "-"
print(f"List letter menjadi {letter}")

#Menghilangkan items
letter.pop(0) #Menghilangkan satu karakter saja pada index (0)
print(f"Setelah index 0 dihilangkan, list letter menjadi >>> {letter}")

letter.remove("b")
print(f"Setelah karakter \"b\" dihilangkan, list letter menjadi >>> {letter}")

del letter[0:2]
print(f"Setelah karakter index(0:2) dihilangkan, list letter menjadi >>> {letter}")

letter.clear()
print(f"Setelah list letter.clear(), list letter menjadi >>> {letter}")
