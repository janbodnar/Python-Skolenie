#!/usr/bin/python

# dictionary_simple.py

words = { 'girl': 'Maedchen', 'house': 'Haus', 'death': 'Tod' }

print(words['house'])

print(words.keys()) #klucove hodnoty
print(words.values())
print(words.items())

print(words.pop('girl'))
print(words)

words.clear()
print(words)