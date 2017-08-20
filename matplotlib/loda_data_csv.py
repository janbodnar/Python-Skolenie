#!/usr/bin/python3

import matplotlib.pyplot as plt

from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('data.csv', unpack=True, delimiter = ',')

plt.plot(x,y)

plt.title('Data')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
