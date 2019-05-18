#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from math import sin

x = np.linspace(0, 10, 1000)

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);
plt.plot(x, np.sin(x))
plt.savefig("test.png")
plt.show()
