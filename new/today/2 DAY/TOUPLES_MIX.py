#!/usr/bin/python

# tuples_mix.py

mix = (1, 2, "solaris", (1, 2, 3))

print("mix[1] :", mix[1])
print("mix[2] :", mix[2])
print("mix[3] :", mix[3])
print("mix[3][0] :", mix[3][0])
print("mix[3][1] :", mix[3][1])
print("mix[3][2] :", mix[3][2])

#####################################################################
# VYPIS 11 TKU
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))

print(mix[3][3][3][1])