# Generating random values


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

## choice

The `choice(seq)` function returns a random element from the non-empty sequence seq.  

```python
import random
print(random.choice('abcdefghij'))
```

AI-generated code. Review and use carefully. More info on FAQ.

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

Please note that the random module uses the pseudo-random number generator which is not suitable for security-sensitive applications. For such use-cases, consider using the secrets module.