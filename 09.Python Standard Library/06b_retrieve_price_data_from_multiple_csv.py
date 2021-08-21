# WORKING WITH CSV FILES
# https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737
# Import all CSV data from specific directory, peek data selling, summarize all the selling.
# https://medium.com/programminginpython-com/python-program-to-calculate-the-sum-of-elements-in-a-list-ed2b80db8268
import csv
from pathlib import Path

path = Path("pooling_data_csv")
file_csv = [p for p in path.glob("*.csv")]
print(file_csv)


# Fungsi untuk WRITE
# with open("data_csv.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transacation_id", "product_id", "prices"])
#     writer.writerow([1, 2000, 35300])
#     writer.writerow([2, 2023, 15700])
#     writer.writerow([3, 2025, 25150])


# # Fungsi untuk read dan display per row
# with open("data_csv.csv") as file_read:
#     reader = csv.reader(file_read)
#     # print(list(reader)) #Membaca isi file dalam bentuk list, tidak dipisah per row
#     for row in reader:
#         print(row)
