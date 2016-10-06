#!/usr/bin/python3

# adding.py

langs = []

langs.append("Python")
langs.append("Perl")
print (langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print (langs)

langs.extend(("JavaScript", "ActionScript"))
print (langs)
