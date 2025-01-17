#!/usr/bin/python
from tkinter.constants import FIRST

# list_modify2.py

first = [1, 2, 3]
second = [4, 5, 6]

first.extend(second)
print(first)

########### APPEND SHOW
# first.append(second)
# print(first)

#prepisanie hodnot
first[0] = 11
first[1] = 22
first[2] = 33
print(first)

print(first.pop(5))  ## POP MMAYANIE
print(first)

