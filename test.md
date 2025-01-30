# Priklady


## Lambda functions

```python
# map
# filter

# negative_vals = []

vals = [-3, 4, 0, 2, -1, 0, 9, -9]

# def is_negative(e):
#     if e < 0:
#         return True

# def is_negative(e):
#     if e < 0:
#         return True


def is_positive(e):
    return e > 0


# for val in vals:
#     if val < 0:
#         negative_vals.append(val)

neg_vals = list(filter(lambda e: e < 0, vals))
print(neg_vals)

pos_vals = list(filter(lambda e: e > 0, vals))
print(pos_vals)
```


## Opakovanie


```python
# print message John Doe is a gardener and live in 
# in New York
name = 'John Doe'
occupation = 'gardener'
city = 'New York'


# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

# calculate sum
data2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10))

# create a new tuple that contains words starting with w or c
words = ['small', 'cup', 'war', 'water', 'cloud', 'warm', 'atom']

# read file words.txt and calculate the number 
# of all ascii characters of all words
```

```
sky
blue
red
brown
pen
dog
forest
```

Riesenie:

```python

# 3916 prezencne

# print message John Doe is a gardener and live in 
# in New York
name = 'John Doe'
occupation = 'gardener'
city = 'New York'

msg = f'{name} is a {occupation} and lives in {city}'
print(msg)


# calculate sum
# split, int
data = "1,2,3,4,5,6,7,8,9,10"

mysum = 0
fields = data.split(',')

print(fields)

for field in fields:
    mysum += int(field)

print(mysum)


# calculate sum
mysum2 = 0
data2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))

for nested in data2:
    for e in nested:
        mysum2 += e

print(mysum2)

# create a new tuple that contains words starting with w or c
# startswith
words = ['small', 'cup', 'war', 'water', 'cloud', 'warm', 'atom']
words_w_c = []

for word in words:
    if word.startswith(('w', 'c')):
        words_w_c.append(word)

words_final = tuple(words_w_c)
print(words_final)

# read file words.txt and calculate the number 
# of all ascii characters of all words
# open

file_name = 'words.txt'
ascii_chars = 0

with open(file_name, 'r') as f:

    for line in f:
        word = line.rstrip()
        ascii_chars += len(word)

    print(ascii_chars)
```


