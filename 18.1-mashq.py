# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:18:59 2022

@author: User
"""

ismlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break
    print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())