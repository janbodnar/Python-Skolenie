#!/usr/bin/python

# bool_fun.py

print(bool(True))
print(bool(False))
print(bool("text"))
print(bool("")) #false
print(bool(" "))  #true
print(bool(' ')) #true
print(bool(0)) #false
print(bool()) #false
print(bool(3))
print(bool(None)) #false
#EMPTY VALUES OR NONE ALWAYS FALSE


#### TOUPLES TIPICKE OPERACIE >> AJ PRE LISTS ################################################

first = (1, 2, 3)
second = (4, 5, 6)

print("len(first) : ", len(first))
print("max(first) : ", max(first))
print("min(first) : ", min(first))
print("first + second :", first + second)
print("first * 3 : ", first * 3)
print("1 in first : ", 1 in first)
print("5 not in second : ", 5 not in second)

#indexing
five = (1, 2, 3, 4, 5)

print("five[0] : ", five[0])
print("five[-1] : ", five[-1])
print("five[-2] : ", five[-2])
print("five[:] : ", five[:])
print("five[0:4] : ", five[0:4])
print("five[1:2] : ", five[1:2])  #result as (2,) >> lebo je to ntica
print("five[:2] : ", five[:2])
print("five[:-1] : ", five[:-1])
print("five[:9] : ", five[:9])