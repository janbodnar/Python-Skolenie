#!/usr/bin/python

import re

text = 'We met in 2013. She must be now about 27 years old.'

pattern = re.compile(r'\d+')

found = re.findall(pattern, text)

if found:
    print('There are {} numbers'.format(len(found)))    
