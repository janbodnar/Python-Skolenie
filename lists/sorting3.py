#!/usr/bin/python3

# sorting3.py

words = ["big", "Blue", "seven", "glass", 
         "Green", "after", "Anctartica"]

words.sort()
print (words)

words.sort(key=str.lower)
print (words)
