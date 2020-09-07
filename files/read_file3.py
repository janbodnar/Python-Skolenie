#!/usr/bin/python

# read_file3.py

with open('works.txt', 'r') as f:

    contents = f.readlines()
    
    for i in contents:
        
        print(i.strip())
