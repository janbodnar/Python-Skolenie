#!/usr/bin/python

import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis = [5, 16, 34, 56, 32, 56, 32, 12, 76, 89]


plt.title("Prices over 10 years")
plt.scatter(x_axis, y_axis, color='darkblue', marker='x', label="item 1")

plt.xlabel("Time (years)")
plt.ylabel("Price (dollars)")

plt.grid(True)
plt.legend()

plt.show()
