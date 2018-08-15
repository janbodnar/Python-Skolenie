#!/usr/bin/python3

import re

words = ('book', 'bookworm', 'Bible', 
    'bookish', 'bookstore', 'boolean')

pattern = re.compile(r'book')

for word in words:
    if re.match(pattern, word):
        print('The {} matches '.format(word))
