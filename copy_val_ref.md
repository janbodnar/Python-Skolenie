# Copy by value vs by reference

In Python, variables are copied by reference for lists, dictionaries, and sets.  
For basic values (integers, strings) and for other immutable objects (tuples) the  
variables are copied by value.  

Copy by reference is used to save memory for large data structures.  

```python
x = 10 
y = x

print(x, y)

y = 11

print(x, y)
```

Assigning `x` to `y` `y = x` creates a copy of the integer value.  Changing `y` later does  
not affect `x`.  


```python
x = [1, 2, 3]
y = x

print(f'x: {x}\ny: {y}')

y[2] = 11

print('----------------------')

print(f'x: {x}\ny: {y}')
```

In case of lists, expression `y = x` creates a new reference to the `x` variable. Modifying `y` also  
modifies `x`.  Now both `x` and `y` point to the same data in memory.  

## Passing arguments to functions

Lists are passed to functions by reference.  

```python
def modify(data):

    for i, _ in enumerate(data):
        data[i] *= 2


vals = [1, 2, 3, 4, 5]

print(vals)
modify(vals)
print(vals)
```

Modifying data inside the function alters the original data.  



