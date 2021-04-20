###FINDING ITEMS
letters = ["a", "b", "c", "d", "d", "e"]
print(f"Berikut adalah isi list letter>>> {letters}")
if "d" in letters: #Jika string "d" ada pada letters
    print(letters.index ("d")) # Print index pertama kemunculan string "d" pada list letter.
print(letters.count("a")) #Menghitung jumlah tampilnya huruf "a"
print(letters.count("d"))  #Menghitung jumlah tampilnya huruf "d"
print(len(letters)) #Menpilkan banyaknya len dari list letters.