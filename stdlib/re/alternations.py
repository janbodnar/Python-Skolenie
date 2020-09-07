#!/usr/bin/python

import re

words = ("Jane", "Thomas", "Robert",
    "Lucy", "Beky", "John", "Peter", "Andy")

pattern = re.compile(r'Jane|Beky|Robert')

for word in words:
    if re.match(pattern, word):
        print(word)
