# EXCERCISE
# Cari cara untuk menentukan karakter mana yag paling sering muncul dari string berikut
import collections
from collections import Counter
sentence = "This is a common interview question"
most_1 = collections.Counter(sentence).most_common(1)[0]
# jika opsi most_commone() maka di list semua karakternya
most_2 = collections.Counter(sentence).most_common()
print(most_1)
print(most_2)
