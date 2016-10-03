#!/usr/bin/python3

# list_modify.py

names = []

names.append("Frank")
names.append("Alexis")
names.append("Erika")
names.append("Ludmila")

print (names)

names.insert(0, "Adriana")
print (names)

names.remove("Frank")
names.remove("Alexis")
del names[1]
print (names)

del names[0]
print (names)
