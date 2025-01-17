#!/usr/bin/python

# continue_kwd.py
##########################################################################
#   VYPISE NEPARNE CISLA

num = 0

while num < 1000:

      num = num + 1

      if num % 2 == 0:  # % operator na zvysok po deleni
         continue #preskoci

      print(num, end=" ")

print()

###########################################################################
#   VYPISE PARNE CISLA

num = 0

while num < 1000:

      num = num + 1

      if num % 2 != 0:  # ALEBO num % 2 == 1
         continue #preskoci

      print(num, end=" ")

print()


