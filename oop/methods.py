#!/usr/bin/python

# methods.py

class Circle:

   pi = 3.141592

   def __init__(self, radius=1):
      self.radius = radius 

   def area(self):
      return self.radius * self.radius * Circle.pi

   def setRadius(self, radius):
      self.radius = radius

   def getRadius(self):
      return self.radius


c = Circle()

c.setRadius(5)
print(c.getRadius())
print(c.area())
