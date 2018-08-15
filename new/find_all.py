#!/usr/bin/python3

import re

text = ('I saw a fox in the wood. The fox had red fur.')

pattern = re.compile(r'fox')

found = re.findall(pattern, text)

for item in found:

    print(item)
