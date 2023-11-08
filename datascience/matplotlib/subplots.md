# Subplots 

It is possible to place multiple charts in a plot via subplots.  
Subplots are created with `subplot` or `subplots` functions.   

The `subplots` creates a figure and a grid of subplots with a single call, 
while providing reasonable control over how the individual plots are created. 

```python
#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# x, y coordinates on sine and cosine curves
x = np.arange(0, 12*np.pi, 0.1)
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

plt.savefig('subplots.png')
```

## Polar subplots 

The `tight_layout` function automatically maintains  
the proper space between subplots.

```python
#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x ** 2)

fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))

# fig.tight_layout(pad=2.0)
fig.tight_layout()

ax1.plot(x, y)
ax2.plot(x, y ** 2)

plt.savefig('subpolars.png')
```



## Creating each subplot separately

We can separately create each subplot with `subplot` function.

```python
#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([6, 8, 2, 11])

plt.subplot(2, 3, 1)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([15, 25, 35, 45])

plt.suptitle('Subplots')

plt.subplot(2, 3, 2)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([2, 9, 11, 11])

plt.subplot(2, 3, 3)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([11, 22, 33, 55])

plt.subplot(2, 3, 4)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([13, 18, 11, 10])

plt.subplot(2, 3, 5)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x, y)

plt.savefig('subplots2.png')
```

## Sharing x axis

Setting the `sharex` option the subplots share the x axis. 

```python
#!/usr/bin/python

import matplotlib.pyplot as plt

data = {'FreeBSD': 4, 'NetBSD': 1, 'Linux': 12, 'Windows': 6, 'Apple': 2}
keys = list(data.keys())
vals = list(data.values())

fig, axs = plt.subplots(3, 1, figsize=(4, 10), sharex=True)
axs[0].bar(keys, vals)
axs[1].scatter(keys, vals)
axs[2].plot(keys, vals)

fig.suptitle('Operating systems in lab')
plt.savefig('subplots.png')
```

## Sharing y axis 

With `sharey` we can share the y axis for all subplots.  
The `set_tick_params` is used to adjust the label size.  

```python
#!/usr/bin/python

import matplotlib.pyplot as plt

data = {'FreeBSD': 4, 'NetBSD': 1, 'Linux': 12, 'Windows': 6, 'Apple': 2}
keys = list(data.keys())
vals = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(keys, vals)
axs[1].scatter(keys, vals)
axs[2].plot(keys, vals)

axs[0].xaxis.set_tick_params(labelsize=7)
axs[1].xaxis.set_tick_params(labelsize=7)
axs[2].xaxis.set_tick_params(labelsize=7)

fig.suptitle('Operating systems in lab')
plt.savefig('subplots.png')
```

## Subplots with labels and titles

```python
#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(3, 3, figsize=(15, 8), sharex=True, sharey=True)

for i, ax in enumerate(axs.flat):
    ax.scatter(*np.random.normal(size=(2, 200)))
    ax.set_title(f'Title {i+1}')

# set labels
plt.setp(axs[-1, :], xlabel='x axis label')
plt.setp(axs[:, 0], ylabel='y axis label')

plt.savefig('subplots.png')
```
