# WORKING WITH CSV FILES
import csv

# Fungsi untuk WRITE
""" with open("data_csv.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transacation_id", "product_id", "prices"])
    writer.writerow([1, 2000, 35300])
    writer.writerow([2, 2023, 15700])
    writer.writerow([3, 2025, 25150])
 """

# Fungsi untuk read dan display per row
with open("data_csv.csv") as file_read:
    reader = csv.reader(file_read)
    # print(list(reader)) #Membaca isi file dalam bentuk list, tidak dipisah per row
    for row in reader:
        print(row)
