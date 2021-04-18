# INFINITE LOOPS
# Loop yang akan terus running, oleh karena itu perlu dibuatkan program break untuk menghentikannya.
while True:  # Skenario tanpa perlu menggunakan string kosong pada variabel command = ""
    command = input(">>>")  # Prompt yg ditampilkan >>>.
    print("ECHO ", command)
    if command.lower() == "quit":  # Ingat : diakhir fugsi IF
        break  # Untuk menghentikan program ketika terdapat command dengan string "quit" diketikkan user
