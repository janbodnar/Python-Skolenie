#!/usr/bin/python

import re

content = '''<p>The <code>pattern</code> is a compiled representation of 
a regular expression.</p>'''

pattern = re.compile(r'</?[a-z]*>')

matches = re.findall(pattern, content)

for match in matches:
    print(match)
