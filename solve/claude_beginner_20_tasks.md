# Claude 20 beginner tasks

```python
# 1
vals = [2, 1, 3, 5, 4]
max_val = ...
min_val = ...
first_val = ...
last_val = ...
assert (max_val, min_val, first_val, last_val) == (5, 1, 2, 4)
print('1 passed')
```

```python
# 2
vals = [10, 20, 30, 40]
total = ...
count = ...
average = ...
assert (total, count, average) == (100, 4, 25.0)
print('2 passed')
```

```python
# 3
name = "python"
upper_name = ...
length = ...
first_letter = ...
assert (upper_name, length, first_letter) == ("PYTHON", 6, "p")
print('3 passed')
```

```python
# 4
vals = [5, 3, 8, 1, 9]
sorted_asc = ...
sorted_desc = ...
assert (sorted_asc, sorted_desc) == ([1, 3, 5, 8, 9], [9, 8, 5, 3, 1])
print('4 passed')
```

```python
# 5
vals = [1, 2, 3, 4, 5]
squared = ...  # list of each value squared, using a list comprehension
assert squared == [1, 4, 9, 16, 25]
print('5 passed')
```

```python
# 6
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = ...  # list comprehension: only even numbers
odds = ...   # list comprehension: only odd numbers
assert (evens, odds) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
print('6 passed')
```

```python
# 7
sentence = "the quick brown fox"
words = ...        # split into a list of words
word_count = ...    # number of words
assert (words, word_count) == (["the", "quick", "brown", "fox"], 4)
print('7 passed')
```

```python
# 8
vals = [3, 1, 4, 1, 5, 9, 2, 6]
unique_vals = ...  # a set of unique values
num_unique = ...
assert (unique_vals, num_unique) == ({1, 2, 3, 4, 5, 6, 9}, 7)
print('8 passed')
```

```python
# 9
vals = [1, 2, 3]
more_vals = [4, 5, 6]
combined = ...      # concatenate the two lists
combined_len = ...
assert (combined, combined_len) == ([1, 2, 3, 4, 5, 6], 6)
print('9 passed')
```

```python
# 10
text = "  hello world  "
stripped = ...
replaced = ...  # replace "world" with "python" (on the stripped text)
assert (stripped, replaced) == ("hello world", "hello python")
print('10 passed')
```

```python
# 11
vals = [1, 2, 3, 4, 5]
reversed_vals = ...  # reversed list (as a list, not a reversed object)
assert reversed_vals == [5, 4, 3, 2, 1]
print('11 passed')
```

```python
# 12
d = {"a": 1, "b": 2, "c": 3}
keys = ...     # list of keys
values = ...   # list of values
b_value = ...  # value for key "b"
assert (keys, values, b_value) == (["a", "b", "c"], [1, 2, 3], 2)
print('12 passed')
```

```python
# 13
vals = [4, 8, 15, 16, 23, 42]
contains_15 = ...   # True if 15 is in vals
index_of_16 = ...    # index of 16 in vals
assert (contains_15, index_of_16) == (True, 3)
print('13 passed')
```

```python
# 14
vals = ["apple", "banana", "cherry"]
joined = ...  # join with ", " as separator
assert joined == "apple, banana, cherry"
print('14 passed')
```

```python
# 15
n = 5
factorial = 1
# write a for loop that multiplies factorial by each number from 1 to n
...
assert factorial == 120
print('15 passed')
```

```python
# 16
vals = [1, 2, 3, 4, 5, 6, 7, 8]
first_three = ...  # slice: first 3 elements
last_three = ...    # slice: last 3 elements
middle = ...         # slice: elements from index 2 to 5 (exclusive)
assert (first_three, last_three, middle) == ([1, 2, 3], [6, 7, 8], [3, 4, 5])
print('16 passed')
```

```python
# 17
vals = [1, 2, 3]
tripled = ...  # list with each value repeated 3 times in a row, e.g. [1,1,1,2,2,2,3,3,3]
...
assert tripled == [1, 1, 1, 2, 2, 2, 3, 3, 3]
print('17 passed')
```

```python
# 18
pairs = [(1, "a"), (2, "b"), (3, "c")]
numbers = ...  # list comprehension: extract just the numbers
letters = ...   # list comprehension: extract just the letters
assert (numbers, letters) == ([1, 2, 3], ["a", "b", "c"])
print('18 passed')
```

```python
# 19
vals = [1, 2, 3, 4, 5]
total_sum = 0
# write a while loop that adds up all values in vals into total_sum
...
assert total_sum == 15
print('19 passed')
```

```python
# 20
def add_one(x):
    ...  # complete this function so it returns x + 1

result = [add_one(v) for v in [1, 2, 3]]
assert result == [2, 3, 4]
print('20 passed')
```

print("\nAll 20 exercises passed!")
```
