# Kurz jazyka Python

## Úvod

1. winget 
2. Terminal
3. Python
4. VS Code

```
pip install ipykernel
```

## Linky


- [JetBrains Python prieskum](https://www.jetbrains.com/lp/devecosystem-2023/python/)
- [VS Code Python doc](https://code.visualstudio.com/docs/python/python-quick-start)
- [C++ vs Python vs Java](https://www.youtube.com/watch?v=hnlz0YYCpBU)
- [Stackoverflow survey](https://survey.stackoverflow.co/2023/#section-admired-and-desired-programming-scripting-and-markup-languages)


## VS Code

- Doplnky
- Python profil
- Príkazová paleta
- Základné nastavenia
- Klávesové skratky
- Spúšťanie Python programov

## Doplnky 

- MS Python
- Jupyter

Všetky doplnky je možné naištalovať pomocou bublín vo VS Code transparentne bez 
toho, aby si to užívateľ uvedomil.  


## Roly 

- Dátový inžinier (data engineer)
- Dátový vedec (data scientist)
- Dátový analytik (data analytic) 

# Základné programovacie postupy

- nemeniteľnosť (immutability)
- funkcionálne programovanie
- list comprehensions
- využitie record typov (data class v Pythone)
- využitie pattern matchingu

## Zopakovanie základov

```python
#!/usr/bin/python

# recapitulation
# recap.py

import random
import sys

# ******************************      
# os module

print(sys.version)

print("******************************") 

# ******************************      
# list, for loop, built-ins

nums = [1, 2, 3, 4, 5]

print("There are {0} elements in the list".format(len(nums)))

for e in nums:
    print(e, end=' ')
    
print()    

print("maximum: {0}".format(max(nums)))
print("maximum: {0}".format(max(nums)))
print("summation: {0}".format(sum(nums)))

# ******************************
# expressions, operators

x = 45
y = 12

z = x * y - 12
print(z)

print(12 / 4 * 3)


# ******************************
# booleans      

male = False
male = bool(random.randint(0, 1))

if male:
   print("We use name John")
else:
   print("We use name Victoria")
   
 
print("******************************") 

# ******************************      
# dictionary   

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print(capitals)


for k, v in capitals.items():
    print("key: {0}, value: {1}".format(k, v))

print("******************************")

# ******************************      
# while loop

i = len(nums) - 1
mysum = 0

while (i >= 0):
    
    mysum += nums[i]
    i -= 1
    

print("summation 2: {0}".format(mysum))

print("******************************")

# ******************************      
# introspection

ab = ()
print(type(ab))
print(dir(ab))
print(ab.__doc__)

print("******************************")

# ******************************      
# sets

set1 = { 'a', 'b', 'c', 'c', 'd' }
set2 = { 'a', 'b', 'x', 'y', 'z' }

print("Set 1:", set1)
print("Set 2:", set2)
print("intersection:", set1.intersection(set2))
print("union:", set1.union(set2))
print("difference:", set1.difference(set2))
print("symmetric difference:", set1.symmetric_difference(set2))
```
