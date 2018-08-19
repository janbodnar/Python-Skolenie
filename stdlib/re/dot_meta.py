#!/usr/bin/python3

import re

words = ('seven', 'even','prevent', 'revenge', 'maven', 
    'eleven', 'amen', 'event')

pattern = re.compile(r'.even')

for word in words:
    if re.match(pattern, word):
        print('The {} matches '.format(word))
