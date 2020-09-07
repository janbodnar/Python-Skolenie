#!/usr/bin/python

import locale

words = ['zem', 'čučoriedka', 'drevo', 'štebot', 'cesta', 'černice', 'ďateľ', 'rum', 'železo', 'prameň', 'sob']
locale.setlocale(locale.LC_COLLATE, ('sk_SK', 'UTF8'))

words.sort(key=locale.strxfrm)

for word in words:
    print(word)
