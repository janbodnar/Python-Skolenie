#!/usr/bin/python

# strippig.py

s = " Eagle  "

s2 = s.rstrip()
s3 = s.lstrip()
s4 = s.strip()

print('{0} {1}'.format(s, len(s)))
print('{0} {1}'.format(s2, len(s2)))
print('{0} {1}'.format(s3, len(s3)))
print('{0} {1}'.format(s4, len(s4)))

###############################################################################
print("   bbb\raaa") # prints aaabbb