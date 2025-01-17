# Priklady

## Opakovanie

```python
# print first, fourth, last, last but one character
msg = 'and old falcon in the sky'

# print first, second, last, last but one word
msg2 = 'and old falcon in the sky'

# create message John Doe is a gardener
# and lives in New York
name = "John Doe"
occupation = "gardener"
city = 'New York'

# calculate the sum of positive values
vals = [1, 0, -3, 4, 5, -6, -7, 3, -1]

# print words that start with w or c
words = ['sky', 'cup', 'water', 'warm', 'spy', 'cloud', 'necessity']
```

### Riesenia

```python

# print first, fourth, last, last but one character
msg = 'and old falcon in the sky'
print(msg[0])
print(msg[3])
print(msg[-1])
print(msg[-2])


# print first, second, last, last but one word
# funkcia split
msg2 = 'an old falcon in the sky'
mywords = msg2.split(' ')
print(mywords[0])
print(mywords[1])
print(mywords[-1])
print(mywords[-2])


# create message John Doe is a gardener
# and lives in New York
# fstring
name = "John Doe"
occupation = "gardener"
city = 'New York'

msg = f'{name} is a {occupation} and lives in {city}'
print(msg)

# calculate the sum of positive values
vals = [1, 0, -3, 4, 5, -6, -7, 3, -1]

mysum = 0

for val in vals:
    if val > 0:
        mysum += val

print(mysum)

# print words that start with w or c
words = ['sky', 'cup', 'water', 'warm', 'spy', 'cloud', 'necessity']

for word in words:
    # if word.startswith(('w', 'c')):
    #     print(word)

    if word.startswith('w') or word.startswith('c'):
        print(word)
```



## String formatting

```python
name = 'Peter'
age = 23
weight = 56.7

# Peter is 23 years old, his weight is 56.7
print('%s is %d years old, his weight is %.3f' % (name, age, weight))
print('{} is {} years old, his weight is {}'.format(name, age, weight))
print(f'{name} is {age} years old, his weight is {weight:.2f}')
```

## Case

```python
total_chars_3c = 0

words = ['sky', 'war', 'Water', 'coin', 'WARM', 'forest']

for word in words:

    # if word.lower().startswith('w'):
    #     total_chars_3c += len(word)

    if word.startswith(('w', 'W')):
        total_chars_3c += len(word)

print(total_chars_3c)
```

---

```python
total_chars_3c = 0

words = ['sky', 'war', 'Water', 'coin', 'WARM', 'forest']

for word in words:

    if word.startswith('w') or word.startswith('W'):
        total_chars_3c += len(word)

print(total_chars_3c)
```


## startswith funkcia

```python
total_chars_w = 0

words = ['sky', 'war', 'water', 'coin', 'warm', 'forest']

for word in words:

    if word.startswith('w'):
        total_chars_w += len(word)
    

print(total_chars_w)
```

---

```python
total_chars_3c = 0

words = ['sky', 'war', 'water', 'coin', 'warm', 'forest']

for word in words:

    if len(word) == 3:
        total_chars_3c += len(word)

print(total_chars_3c)
```

## total chars

```python
total_chars = 0

words = ['sky', 'war', 'water', 'coin', 'forest']

for word in words:
    total_chars = total_chars + len(word)

print(total_chars)
```


## Unique words

```python
words = ("coin", "coin", "book", "pencil", "spoon", "coin", "paper")
print(words)

unique_words = set(words)
print(unique_words)

print(type(words))
print(type(unique_words))
```

## not operator

```python
words = ['sky', 'war', 'rock']

if 'sky' in words:
    print('word sky is in the list')

if 'water' not in words:
    print('word water is not in the list')
```

## Pretypovanie

```python
x = 2
word = " apples"

# '2' + " apples"
msg = str(x) + word

print(msg)

x = '10'
y = '11'

print(int(x) + int(y))
```


## if conditions

```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
elif r < 0:
    print('The r variable is negative')
else:
    print('The r variable is zero')

# if r < 0:
#     print('The r variable is negative')
#
# if r == 0:
#     print('The r variable is zero')
```
