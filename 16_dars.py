# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:55:10 2022

@author: User
"""

malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
    
#for malibu in malibus[:3]:
 #   malibu['rang']='qizil'
    
#for malibu in malibus[3:6]:
  
    #malibu['rang']='qora'
for malibu in malibus:
    if malibu['korobka']=='avto':
       malibu['narh']=40000
    else:
        malibu['narh']=35000
        
       