#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# x, y coordinates on sine and cosine curves
x = np.arange(0, 4 * np.pi, 0.1)
f_sin = np.sin(x)
f_cos = np.cos(x)

# first subplot with height 2 and width 1
plt.subplot(2, 1, 1)

plt.plot(x, f_sin)
plt.title('Sine')

# second subplot
plt.subplot(2, 1, 2)
plt.plot(x, f_cos)
plt.title('Cosine')

plt.show()
