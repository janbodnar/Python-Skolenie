#!/usr/bin/python

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish','cookbook', 'bookstore', 'pocketbook')

pattern = re.compile(r'book')

for word in words:
    if re.match(pattern, word):
        print('The {} matches '.format(word))
