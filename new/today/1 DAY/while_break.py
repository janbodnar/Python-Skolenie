#!/usr/bin/python

# break >> na ukoncenie nekonecneho cyklu

import random

while True:

    val = random.randint(1, 30)
    print(val, end=" ") # end pomoze vypisat hodnoty na jednom riadku
    #print(val) #vypise hodnoty v stlpci

    if val == 22:
        break

print()