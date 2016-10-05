#!/usr/bin/python3

# letters.py

sentence = "There are 22 apples"

alphas = 0
digits = 0
spaces = 0

for i in sentence:
    
   if i.isalpha():
      alphas += 1
      
   if i.isdigit():
      digits += 1
      
   if i.isspace():
      spaces += 1

print ("There are", len(sentence), "characters")
print ("There are", alphas, "alphabetic characters")
print ("There are", digits, "digits")
print ("There are", spaces, "spaces")
