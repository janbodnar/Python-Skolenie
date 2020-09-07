#!/usr/bin/python

with open('words.txt') as f:

    lines = f.readlines()

    for line in lines:
        print(line.rstrip())
