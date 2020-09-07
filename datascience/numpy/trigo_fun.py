#!/usr/bin/python

import numpy as np

a = np.array([0, 30, 45, 60, 90, 120]) 

# Convert to radians by multiplying with pi/180 
print(np.sin(a*np.pi/180))
print(np.cos(a*np.pi/180))
print(np.tan(a*np.pi/180)) 
