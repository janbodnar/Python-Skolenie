#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2.5 * np.pi * t)

plt.plot(t, s)
 
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

plt.title('Sine Wave')
plt.grid(True)

plt.show()
