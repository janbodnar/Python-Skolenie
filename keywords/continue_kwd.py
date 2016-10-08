#!/usr/bin/python3

# continue_kwd.py

import random

num = 0

while (num < 1000):

   num = num + 1
   
   if (num % 2) == 0:
      continue
      
   print (num, end=" ")
