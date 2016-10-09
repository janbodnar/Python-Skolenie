#!/usr/bin/python3

# class_attribute.py

class Cat:
   species = 'mammal'

   def __init__(self, name, age):
       
      self.name = name
      self.age = age


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print (missy.name, missy.age)
print (lucky.name, lucky.age)

print (Cat.species)
print (missy.__class__.species)
print (lucky.__class__.species)
