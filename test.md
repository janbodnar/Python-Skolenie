# Priklady


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
