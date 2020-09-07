#!/usr/bin/python

import numpy as np
from scipy.spatial.distance import pdist, squareform

# three points
points = np.array([[-1, 1], [1, 0], [2, 0]])

# distance between all points
d = squareform(pdist(points, 'euclidean'))
print(d)
