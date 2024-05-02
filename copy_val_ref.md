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

If we do not want to modify the original data, we pass a copy of the data  
to the function.  

```python
def modify(data):

    for i, _ in enumerate(data):
        data[i] *= 2

    print(f'inside modify: {data}')


vals = [1, 2, 3, 4, 5]

print(vals)
modify(vals[:])
modify(vals.copy()) # vals[:] and vals.copy do the same
print(vals)
```

We pass a copy of `vals` to the `modify` function with `vals[:]` or `vals.copy`.  


## Modify data in-place or create a modified copy

Often, we have an option to modify data in-place or create a modified copy using different functions.  
For instance, we have `sort` & `reverse` functions that modify in-place, and `sorted` & `reversed`  
that create a modified copy.  

```python
vals = [8, 7, 6, 0, -1, -2, 2, 1, -3, 4, 3, 5]

print(vals)
vals.sort()
print(vals)
```

The `sort` function sorts data in-place. 

```python
vals = [8, 7, 6, 0, -1, -2, 2, 1, -3, 4, 3, 5]

print(vals)
vals_s = sorted(vals)
print(vals_s)
print(vals)
```

The `sorted` function creates a sorted copy of the data; the original values are not modified.  





