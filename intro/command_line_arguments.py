#!/usr/bin/python3

# command_line_arguments.py

import sys

print ("Script name:", sys.argv[0])
print ("Arguments:", end=" ")

for arg in sys.argv[1:]:
    print (arg, end=" ")
    
print ()
