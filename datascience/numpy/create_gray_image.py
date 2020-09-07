#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# sample 2D array    
x = np.random.random((100, 100)) 

plt.imshow(x, cmap="gray")
plt.show()
