#!/usr/bin/python3

# pickle_ex.py

import pickle

class Person(object):
    
   def __init__(self, name, age):
       
      self.name = name
      self.age = age

   def getName(self):
       
      return self.name

   def getAge(self):
       
      return self.age


person = Person('Monica', 15)
print(person.getName())
print(person.getAge())

with open('monica', 'wb') as f:
    pickle.dump(person, f)

with open('monica', 'rb') as f2:
    monica = pickle.load(f2)

print(monica.getName())
print(monica.getAge())
