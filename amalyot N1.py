# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:04:27 2022

@author: User
"""
#AMALYOT N#1
def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {'ism':ism,
             'familiya':familiya,
             'tyil':tyil,
             'yoshi':2020-tyil,
             'tjoy':tjoy,
             'email':email,
             'telefon':tel}
    return mijoz

print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['email']}",
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
    
    