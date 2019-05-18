#!/usr/bin/env python3

import numpy as np

# picking random words with specified probabilities
# for each word

words = ['falcon', 'rabbit', 'sky', 'wood', 'forest']

words2 = np.random.choice(words, 5, p=[0.5, 0.1, 0.1, 0.2, 0.1])
print(words2)
