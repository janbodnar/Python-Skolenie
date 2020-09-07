#!/usr/bin/python

# modifying.py

langs = ["Python", "Ruby", "Perl"]

langs.pop(2)
langs.insert(2, "PHP")
print (langs)

langs[2] = "Perl"
print (langs)
