# Python assert keyword

The assert keyword in Python is used to set a checkpoint in your code that tests  
a condition. If the condition evaluates to `True`, the program continues to  
execute normally. If the condition evaluates to `False`, an `AssertionError`  
exception is raised, halting the program and typically indicating a bug in the  
code.

```python
assert condition, message
```

- condition: This is the condition you want to test. If it evaluates to `True`,  
  the program continues. If it evaluates to `False`, an `AssertionError` is  
  raised.  
- message (optional): An optional message to provide more information about the  
  assertion error.


```
$ py -O main.py
```

Assertions can be turned off with the `-O` flag.

## Example Usage

### Basic Example

```python
x = 10
assert x > 5, "x should be greater than 5"
print("Assertion passed")
```

In this example, since x is indeed greater than 5, the assertion passes and  
"Assertion passed" is printed.

### Example with Failing Condition

```python
y = 2
assert y > 5, "y should be greater than 5"
print("This will not be printed")
```

Here, since `y` is not greater than 5, the assertion fails and raises an  
`AssertionError` with the message "y should be greater than 5".

### Example in a Function

```python
def divide(a, b):
    assert b != 0, "The divisor 'b' must not be zero"
    return a / b

print(divide(10, 2))  # This works
print(divide(10, 0))  # This raises an AssertionError
```

In this example, the `assert` keyword ensures that the divisor is not zero  
before performing the division. If b is zero, an `AssertionError` is raised with  
the message "The divisor 'b' must not be zero".  

### Parameter types

We can use the `assert` statement to check the type of the parameters at the  
beginning of the function.  

```python
def my_function(a, b):
    assert isinstance(a, int), "Parameter 'a' must be an integer"
    assert isinstance(b, str), "Parameter 'b' must be a string"
    # Function logic here
    print(f"a: {a}, b: {b}")

# Example usage
my_function(5, "hello")  # This works
my_function(5, 10)  # This raises AssertionError: Parameter 'b' must be a string
```


### Example in Unit Tests

Assertions are often used in unit tests to validate the behavior of functions:

```python
def test_sum():
    result = sum([1, 2, 3])
    assert result == 6, f"Expected 6 but got {result}"

test_sum()
```

In this unit test example, the `assert` keyword is used to ensure that the `sum`  
function returns the expected result. If the result is not as expected, an  
`AssertionError` is raised with a descriptive message.  

## Summary

The `assert` keyword is a handy tool for testing and debugging your code,  
ensuring that certain conditions hold true. It provides a simple yet powerful  
way to catch bugs early in the development process.  


## Unit tests

```
pip install pytest
```

The `algo.py` module:

```python
def max(values):

  _max = values[0]

  for val in values:
      if val > _max:
          _max = val

  return _max


def min(values):

  _min = values[0]

  for val in values:
      if val < _min:
          _min = val

  return _min
```

The `min_max_test.py`:  

```python
import algo

def test_min():
    values = (2, 3, 1, 4, 6)

    val = algo.min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)

    val = algo.max(values)
    assert val == 6
```