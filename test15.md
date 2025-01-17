# Priklady


## Filter & unique with Pandas

```python
import pandas as pd

file_name = 'words.txt'

# Načítaj súbor do DataFrame
df = pd.read_csv(file_name, header=None, names=['word'])

print(df)

# Odstráň medzery okolo slov
df['word'] = df['word'].str.strip()

# Filtrovanie slov s presne 3 písmenami
words_3c = df.query('word.str.len() == 3')['word']
#
# # Odstránenie duplicít
unique_words = words_3c.drop_duplicates()
#
# print(words_3c.tolist())
print(unique_words.tolist())
```


## Filter & unique with basic Python

```python
# nacitat subor words.txt
# filtrovat slova majuce 3 znaky -> words_3c zoznam
# odstranit duplicity

# open
# for loop
# odstranit bliele znaky pomocou strip
# aplikovat filter funkciu

file_name = 'words.txt'

with open(file_name, 'r') as f:

    lines = []

    for line in f:
        lines.append(line.strip())

    # lines = f.readlines()
    # print(lines)

    # words = list(map(str.strip, lines))
    # print(words)

    words_3c = list(filter(lambda e: len(e) == 3, lines))
    print(words_3c)

    unique_words = set(words_3c)
    print(unique_words)
```



## lambda functions

```python
def has_three_chars(e):
    return len(e) == 3

def starts_with_w_or_c(word):
    # return word.startswith('w') or word.startswith('c')
    return word.startswith(('w', 'c'))

words = ['sky', 'war', 'water', 'cloud', 'pen', 'rock', 'book']

words_3c = list(filter(lambda e: len(e) == 3, words))
print(words_3c)

words_w_c = list(filter(lambda e: e.startswith(('w', 'c')), words))
print(words_w_c)
```




## filter words

```python
def has_three_chars(e):
    return len(e) == 3

words = ['sky', 'war', 'water', 'cloud', 'pen', 'rock', 'book']

words_3c = list(filter(has_three_chars, words))
print(words_3c)
```

```python
def has_three_chars(e):
    return len(e) == 3

def starts_with_w_or_c(word):
    # return word.startswith('w') or word.startswith('c')
    return word.startswith(('w', 'c')) 

words = ['sky', 'war', 'water', 'cloud', 'pen', 'rock', 'book']

words_3c = list(filter(has_three_chars, words))
print(words_3c)

words_w_c = list(filter(starts_with_w_or_c, words))
print(words_w_c)
```


## Filter numbers 

```python
def is_positive(e):
    return e > 0

def is_negative(e):
    return e < 0


vals = [-3, 0, 1, 2, 3, -7, -5, 9, 8]

positive = list(filter(is_positive, vals))
print(positive)

negative = list(filter(is_negative, vals))
print(negative)
```


## Sum of CSV data

```python
values = []

with open(file_name, 'r') as f:

    for line in f:
        stripped_line = line.strip()
        fields = stripped_line.split(',')
        values.extend(list(map(int, fields)))


    print(values)
    # words = list(map(str.strip, lines))
    # print(words)

    print(sum(values))
```

Using Pandas


```python
import pandas as pd

file_name = 'data.csv'
df = pd.read_csv(file_name, header=None)

print(df.to_string(index=False, header=False))

total_sum = df.values.sum()
print(total_sum)
```



## Read and clean words

```python
file_name = 'words.txt'

with open(file_name, 'r') as f:
    lines = f.readlines()
    print(lines)

    words = list(map(str.strip, lines))
    print(words)
```


## map function

```python
def twice(e):
    return e * 2

def cube(e):
    return e * e * e


vals = [1, 2, 3, 4, 5]

data = list(map(twice, vals))
print(data)

data = list(map(cube, vals))
print(data)
```

---

```python
words = ['sky\n', 'cloud\n', 'new\n', 'book\n', 'forest\n']

data = list(map(str.strip, words))
print(words)
print(data)
```




## Table of math functions

Table summarizing the functions available in the `math` module of Python:

| **Category**                | **Function**                                                   |
|-----------------------------|----------------------------------------------------------------|
| **Arithmetic functions**    | `math.ceil(x)`, `math.floor(x)`, `math.trunc(x)`, `math.factorial(x)`, `math.fmod(x, y)` |
| **Power and logarithmic functions** | `math.exp(x)`, `math.log(x[, base])`, `math.log10(x)`, `math.sqrt(x)` |
| **Trigonometric functions** | `math.sin(x)`, `math.cos(x)`, `math.tan(x)`, `math.asin(x)`, `math.acos(x)`, `math.atan(x)`, `math.atan2(y, x)` |
| **Hyperbolic functions**    | `math.sinh(x)`, `math.cosh(x)`, `math.tanh(x)`, `math.asinh(x)`, `math.acosh(x)`, `math.atanh(x)` |
| **Angle conversion functions** | `math.degrees(x)`, `math.radians(x)`                      |
| **Special functions**       | `math.gamma(x)`, `math.lgamma(x)`                             |
| **Constants**               | `math.pi`, `math.e`                                           |



## List of math functions 

Certainly! The `math` module in Python provides a variety of mathematical functions. Here are some of   
the commonly used functions in the standard `math` module:

1. **Arithmetic functions**:
    - `math.ceil(x)`: Returns the smallest integer greater than or equal to x.
    - `math.floor(x)`: Returns the largest integer less than or equal to x.
    - `math.trunc(x)`: Truncates x to the nearest integer towards zero.
    - `math.factorial(x)`: Returns the factorial of x.
    - `math.fmod(x, y)`: Returns the remainder of x divided by y.

2. **Power and logarithmic functions**:
    - `math.exp(x)`: Returns e raised to the power of x.
    - `math.log(x[, base])`: Returns the logarithm of x to the given base.
    - `math.log10(x)`: Returns the base-10 logarithm of x.
    - `math.sqrt(x)`: Returns the square root of x.

3. **Trigonometric functions**:
    - `math.sin(x)`: Returns the sine of x (x is in radians).
    - `math.cos(x)`: Returns the cosine of x (x is in radians).
    - `math.tan(x)`: Returns the tangent of x (x is in radians).
    - `math.asin(x)`: Returns the arc sine of x.
    - `math.acos(x)`: Returns the arc cosine of x.
    - `math.atan(x)`: Returns the arc tangent of x.
    - `math.atan2(y, x)`: Returns atan(y / x), in radians.

4. **Hyperbolic functions**:
    - `math.sinh(x)`: Returns the hyperbolic sine of x.
    - `math.cosh(x)`: Returns the hyperbolic cosine of x.
    - `math.tanh(x)`: Returns the hyperbolic tangent of x.
    - `math.asinh(x)`: Returns the inverse hyperbolic sine of x.
    - `math.acosh(x)`: Returns the inverse hyperbolic cosine of x.
    - `math.atanh(x)`: Returns the inverse hyperbolic tangent of x.

5. **Angle conversion functions**:
    - `math.degrees(x)`: Converts angle x from radians to degrees.
    - `math.radians(x)`: Converts angle x from degrees to radians.

6. **Special functions**:
    - `math.gamma(x)`: Returns the Gamma function at x.
    - `math.lgamma(x)`: Returns the natural logarithm of the absolute value of the Gamma function at x.

7. **Constants**:
    - `math.pi`: The mathematical constant π.
    - `math.e`: The mathematical constant e.









## Read and clean words

```python
file_name = 'words.txt'

with open(file_name, 'r') as f:

    lines = f.readlines()
    print(lines)

    cleaned = []

    for line in lines:
        cleaned.append(line.strip())

    print(cleaned)
```

```python
file_name = 'words.txt'

with open(file_name, 'r') as f:
    cleaned = []
    for line in f:
        cleaned.append(line.strip())

    print(cleaned)
```


## Word frequencies

```python
from collections import Counter

# Read the file
with open('thermopylae.txt', 'r') as file:
    text = file.read()

# Split the text into words
words = text.split()

# Calculate the frequency of each word
word_frequencies = Counter(words)

# Print the frequencies
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
```



```
# vypis 11 pomocou indexacie
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
```

```python
# print message with fstring
# John Doe is 45 years old and he is a gardener
name = 'John Doe'
age = 45
occupation = 'gardener'


# print 1,2, last element
words = ['sky', 'den', 'war', 'town', 'rock']

# calculate sum using for loop
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# create a list of values 500 - 1000 and sum it
```



## Strings 

```python
word = 'eagle'

print(word + " has " + str(len(word)) + " characters")
print(word, "has", len(word), "characters")
print(f'{word} has {len(word)} characters')
```

## Quotes

```python
print("There are many stars.")
print("He said, \"Which one is your favourite?\"")

print('There are many stars.')
print('He said, "Which one is your favourite?"')

print('The film was \'great\'')
print("The film was 'great'")
```


## Nested lists

```python
nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mysum = 0

for nested in nums:

    for e in nested:
        mysum += e
        print(e, end=' ')

    print()

print(mysum)
```


## Ternary operator 

```python
# ternary.py

age = 31

# adult = True if age >= 18 else False
#
# print("Adult: {0}".format(adult))
# print(f"Adult: {adult}")

if age >= 18:
    adult = True
else:
    adult = False

print("Adult: {0}".format(adult))
print(f"Adult: {adult}")
```


## Booleans


```python
words = ['sky', 'blue', 'war', 'water', 'system', 'small']
# print all words starting with 's' or 'w'
for word in words:
    if word.startswith('s') or word.startswith('w'):
        print(word)
```


```python
word = 'falcon'

words = ['sky', 'blue', 'war', 'water']

if word in words:
    print(f'{word} is in the list')

if word not in words:
    print(f'{word} is not in the list')
```
