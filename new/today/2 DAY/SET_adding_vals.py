#!/usr/bin/python

set1 = {1, 2}
set1.add(3)
set1.add(4)

set2 = {1, 2, 3, 4, 6, 7, 8}
set2.remove(8)

print(set1)
print(set2)

print("Is set1 subset of set2 ? :", set1.issubset(set2))
print("Is set1 superset of set2 ? :", set1.issuperset(set2))

set1.clear()
print(set1)