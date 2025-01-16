# Priklady

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
