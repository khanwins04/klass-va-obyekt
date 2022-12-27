# -*- coding: utf-8 -*-
"""RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
Created on Sat Apr  9 22:18:09 2022

@author: User
"""

#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
   # talaba = talabalar.pop()
   # baho = input(f"{talaba.title()}ning bahosini kiriting: ")
   # print(f"{talaba.title()} baholandi")
   # baholangan_talabalar[talaba] = baho
    
#savat =[]
#while True:
    #mahsulot = input("Savatga mahsulot qo'shing:")
    #savat.append(mahsulot)
    #javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    #if javob != 'ha':
     #   break
    
#buyurtmalar = ['olma','anjir','uzum','qovun']
#mahsulotlar = {'olma':20000,
 #              'shaftoli':25000,
  #            'tarvuz':18000,
   #            'uzum':22000}
#
#while buyurtmalar:
 #   buyurtma = buyurtmalar.pop()
  #  if buyurtma in mahsulotlar.keys():
   #     narh = mahsulotlar[buyurtma]
    #    print(f"{buyurtma.title()} - {narh} so'm")
    #else:
     #   print(f"Bizda {buyurtma} yo'q")
     
     
     
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")