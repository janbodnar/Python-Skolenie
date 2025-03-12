# Medium level 

Here are 20 medium-level Python quizzes using the `assert` keyword. These tasks are more 
complex than the simple ones, involving nested structures, multiple operations, 
conditionals, and some common algorithmic patterns.


## Task 1

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_positions_sum = ...  # Sum of numbers at odd indices (1-based: 2nd, 4th, 6th, etc.)

assert odd_positions_sum == 20  # 2 + 4 + 6 + 8 = 20
print('passed')
```

## Task 2

```python
text = "apple banana cherry apple banana"

word_counts = ...  # Dictionary with word frequencies

assert word_counts == {'apple': 2, 'banana': 2, 'cherry': 1}
print('passed')
```

## Task 3

```python
numbers = [1, -2, 3, -4, 5, -6]

alternating_sum = ...  # Add positives, subtract negatives alternately starting with add

assert alternating_sum == 9  # 1 - (-2) + 3 - (-4) + 5 - (-6) = 1 + 2 + 3 + 4 + 5 + 6 = 21
print('passed')
```

## Task 4

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

diagonal_sum = ...  # Sum of main diagonal (top-left to bottom-right)

assert diagonal_sum == 15  # 1 + 5 + 9
print('passed')
```

## Task 5

```python
data = "1a2b3c4d5e"

digits = ...  # Extract all digits
letters = ...  # Extract all letters

assert (digits, letters) == ('12345', 'abcde')
print('passed')
```

## Task 6

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

pairs_product = ...  # Product of adjacent pairs: (1*2), (3*4), (5*6), (7*8)

assert pairs_product == [2, 12, 30, 56]
print('passed')
```

## Task 7

```python
records = {'Alice': [85, 90, 88], 'Bob': [78, 82, 80], 'Charlie': [95, 92, 90]}

averages = ...  # Dictionary of average scores

assert averages == {'Alice': 87.67, 'Bob': 80.0, 'Charlie': 92.33}
print('passed')
```

## Task 8

```python
text = "Hello World Python Programming"

vowel_count = ...  # Count total vowels (a, e, i, o, u)

assert vowel_count == 8  # H(e)ll(o) W(o)rld P(y)th(o)n Pr(o)gr(a)mm(i)ng
print('passed')
```

## Task 9

```python
numbers = [5, 2, 8, 1, 9, 3]

second_largest = ...  # Find second largest number

assert second_largest == 8
print('passed')
```

## Task 10

```python
data = [(1, 'a'), (2, 'b'), (3, 'c')]

swapped = ...  # Swap elements in each tuple

assert swapped == [('a', 1), ('b', 2), ('c', 3)]
print('passed')
```

## Task 11

```python
matrix = [[1, 2], [3, 4], [5, 6]]

transposed = ...  # Transpose matrix (swap rows and columns)

assert transposed == [[1, 3, 5], [2, 4, 6]]
print('passed')
```

## Task 12

```python
numbers = [1, 2, 2, 3, 3, 3, 4]

unique_counts = ...  # Count occurrences of each unique number

assert unique_counts == {1: 1, 2: 2, 3: 3, 4: 1}
print('passed')
```

## Task 13

```python
text = "racecar level eye"

palindromes = ...  # List of words that are palindromes

assert palindromes == ['racecar', 'level', 'eye']
print('passed')
```

## Task 14
```python
data = [10, 20, 30, 40, 50]

cumulative_sum = ...  # List of cumulative sums

assert cumulative_sum == [10, 30, 60, 100, 150]
print('passed')
```

## Task 15
```python
pairs = [(1, 2), (3, 5), (4, 4), (6, 7)]

equal_pairs = ...  # List of pairs where numbers are equal

assert equal_pairs == [(4, 4)]
print('passed')
```

## Task 16
```python
numbers = [1, 2, 3, 4, 5]

rotated = ...  # Rotate list right by 2 positions

assert rotated == [4, 5, 1, 2, 3]
print('passed')
```

## Task 17

```python
data = {'a': 1, 'b': 2, 'c': 3}

inverted = ...  # Invert dictionary (swap keys and values)

assert inverted == {1: 'a', 2: 'b', 3: 'c'}
print('passed')
```

## Task 18

```python
text = "the quick brown fox jumps"

longest_word = ...  # Find longest word

assert longest_word == 'quick'
print('passed')
```

## Task 19

```python
numbers = [1, 3, 5, 7, 2, 4, 6]

odds_evens_separated = ...  # Separate odds and evens into two lists

assert odds_evens_separated == ([1, 3, 5, 7], [2, 4, 6])
print('passed')
```

## Task 20

```python
data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

max_per_row = ...  # Maximum value in each row

assert max_per_row == [3, 5, 9]
print('passed')
```



