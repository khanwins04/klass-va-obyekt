# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 11:50:24 2022

@author: Green IT Serves
"""

matn = "Assalomu aleykum"

class Kompyuter:
 def __init__ (self,model, ram, hdd, gpu, cpu):
   self.model = model  
   self.ram = ram
   self.hdd = hdd
   self.gpu = gpu
   self.cpu = cpu

 def info(self):
      inf = f"{self.model}, RAM:{self.ram}, HDD:{self.hdd}, CPU:{self.cpu}"
      return inf
      
macbook = Kompyuter("Apple Macbook", "8GB","512GB", "M1", "M1")

