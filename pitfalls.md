# Pitfalls

## UnboundLocalError

```python
count = 0

def increment():
    count += 1  # UnboundLocalError
    # global count
    # count = count + 1

increment()
increment()
increment()
increment()
increment()

print(count)
```

## Default lists

```python
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] (unexpected)
```


## Shadowing 

```python
list = [1, 2, 3, 4, 5]  # Shadowing the built-in 'list'

# Trying to use the built-in list function now will result in an error
new_list = list((6, 7, 8))  # TypeError: 'list' object is not callable
print(new_list)
```
