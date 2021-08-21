### SHORT CIRCUIT EVALUATIONS
hi_income = bool(int(input(" Apakah anda memiliki income yg tinggi? (1/0)")))
good_credit= bool(int(input("Apakah score credit anda baik?  (1/0)")))
student = bool(int(input("Apakah anda berstatus pelajar? (1/0)")))

if hi_income and good_credit and not student:
    print("Anda berhak mengajukan kredit")
else:
    print("Maaf, anda belum berhak mengajukan kredit:")
if student == True :
    print("Karena anda masih berstatus pelajar.")
elif good_credit == False:
    print("Karena score credit anda kurang layak.")
elif hi_income == False:
    print("Karena penghasilan anda kurang memadai.")
else:
    print("")
# Dalam logical operator setiap argumen bersifat short ciscuit, pada logic AND begitu menemui salah satu variabel bernilai False 
# maka output akan false apapun nilai variabel setelahnya. 
# Begitupun pada logic OR begitu menemui salah satu variabel bernilai True maka output akan True apapun nilai variabel setelahnya.

# Trik untuk membuat print evaluasi dengan membalik urutan, variabel paling belakang dievaluasi pertama!