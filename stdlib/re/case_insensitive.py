#!/usr/bin/python

import re

words = ('dog', 'Dog', 'DOG', 'Doggy')

pattern = re.compile(r'dog', re.IGNORECASE)

for word in words:
    if re.match(pattern, word):
        print('{} matches'.format(word))
