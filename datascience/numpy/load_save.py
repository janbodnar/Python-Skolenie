#!/usr/bin/python

import numpy as np

a = np.array([1,2,3,4,5]) 

np.save('data', a)

b = np.load('data.npy') 
print(b)

#
# a = np.array([1,2,3,4,5]) 
# np.savetxt('data.txt',a) 

# b = np.loadtxt('data.txt') 
# print(b) 
