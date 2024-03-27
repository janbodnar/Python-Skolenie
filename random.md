# Generating random values

*Random number generator (RNG)* generates a set of values that do not display any distinguishable  
patterns in their appearance. The random number generators are divided into two categories:  
hardware random-number generators and pseudo-random number generators. Hardware random-number  
generators are believed to produce genuine random numbers. Pseudo-random number generators  
generate values based on software algorithms. They produce values that look random. But these  
values are deterministic and can be reproduced, if the algorithm is known.

In computing, random generators are used in gambling, gaming, simulations, or cryptography.  

To increase the quality of the pseudo random-number generators, operating systems use  
environmental noise collected from device drivers, user input latency, or jitter from one or  
more hardware components. This is the core of the cryptographically secure pseudo-random  
number generators.

> For security purposes, cryptographically secure pseudo-random number generators must be used.  

## random 

This function returns a random float number between 0.0 to 1.0. The function doesn’t  
need any arguments.


```python
import random
print(random.random())
```

## randint

`randint(a, b)`  

This function returns a random integer between the two integers `a` and `b` inclusive.


```python
import random
print(random.randint(1, 10))
```

## uniform

The `uniform(a, b)` function returns a random float number between two given parameters    
`a` (inclusive) and `b` (exclusive).


```python
import random
print(random.uniform(1, 10))
```

## randrange

The `randrange(start, stop, step)` function returns a randomly selected element from the  
range created by the start, stop, and step arguments. The stop parameter is required while  
the others are optional.


```python
import random
print(random.randrange(0, 101, 10))
```

creating a list of random vals

```python
import random

rvals = [random.randrange(10, 110, 10) for _ in range(10)]
print(rvals)
```

## choice

The `choice(seq)` function returns a random element from the non-empty sequence seq.  

```python
import random

print(random.choice('abcdefghij'))
```

We can specify population sample `k` and probability weights.  

```python
import random

res = random.choices('abcdef', k=3, weights=[1, 5, 3, 1, 1, 10])
print(res)
```


## shuffle

The `shuffle(seq)` function shuffles the sequence seq in place.  


```python
import random

list = [20, 16, 10, 5];
random.shuffle(list)
print(list)
```

## sample

The `sample(population, k)` function returns a `k` length new list of elements chosen  
from the population sequence or set.

```python
import random
print(random.sample(range(10, 30), 3))
```

