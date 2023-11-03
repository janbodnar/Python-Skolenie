# Python-Skolenie

Materiály a príklady pre školenie jazyka Python.   [English version](#python-course)

## Požiadavky

Školenie nevyžaduje žiadne špeciálne znalosti okrem schopnosti inštalácie programov  
a používania terminálu. Akákoľvek skúsenosť s programovaním je vítaná. 

## Inštalácie

- Python 3.10+
- VS Code 
- Python plugin pre Code

Pri inštalácii Pythonu (platí pre Windows), nezabudnite zaškrnúť voľbu *add to PATH*.

## Rozvrh

## Python základy

- Úvod
- Interaktívny Python
- Lexikálna štruktúra
- Dátové typy
- Operátory
- Riadenie behu programu
- Reťazce
- Zoznamy a slovníky
- Funkcie

## Python základy II

- Zopakovanie základov
- Stručný prehľad OOP
- Moduly
- Balíčky
- Práca so súbormi
- Pokročilá práca s funkciami
- Základy funkcionálneho programovania
- Pip manažér
- Jupyter notebooky
- Štandardná knižnica jazyka Python
  

Kontakt na školiteľa: jan.bodnar(@)gmail.com, 0903 102 418.




## Python Course

Python materials and code examples for the Python course.  

## Requirements 

There are no special requirements other than the ability to download and install programs and  
use the terminal.  

## Outline

- Introduction
- Interactive Python
- Lexical structure
- Data types
- Operators
- Control flow
- Strings
- Lists
- Dictionaries
- Functions

## Installations

- Python 3.10+
- VS Code or Codium
- Python extension for Code

You can bring your own notebook or use the classroom computer. When you install Python, don't forget  
to check the add to `PATH` option.  

```python
from io import StringIO

import requests
import csv
from dataclasses import dataclass

@dataclass
class User:
    name: str
    occupation: str
    age: int


url = 'https://webcode.me/users.csv'
req = requests.get(url)

content = str(req.content, encoding='utf8')

f = StringIO(content)
reader = csv.DictReader(f)

users = []

for user in reader:
    users.append(User(user['name'], user['occupation'], user['age']))

print(users)
```
