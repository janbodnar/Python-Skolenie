# Priklady

```python
# utils.py

def calculate_max(data):
    return max(data)
    

def calculate_min(data):
    return min(data)

def calculate_sum(data):
    return sum(data)
```

```python
import random
import utils

# main.py

data = []

for i in range(100):
    r = random.randint(-100, 100)
    data.append(r)

maximum = utils.calculate_max(data)
minimum = utils.calculate_min(data)
mysum = utils.calculate_sum(data)


print(f'the maximum of random values is {maximum}')
print(f'the minimum of random values is {minimum}')
print(f'the sum of random values is {mysum}')
```


## recap

```python
data = []

# generate 100 random values (random module)
# create calcuate_max, calculate_min, calculate_sum in utils.py
# use fstrings to generate final output

# --------------------------------

file_name = 'thermopylae.txt'

n_vowels = 0
n_consonants = 0

with open(file_name) as f:
    contents = f.read()
    
    for c in contents:
        
        if c in 'aeiouAEIOU':
            n_vowels += 1
        
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            n_consonants += 1


print(f'there are {n_vowels} vowels')
print(f'there are {n_consonants} consonants')


# --------------------------------

file_name = 'unix-words.txt'

# read the file and calculate the number of all words and 
# the number of words starting with 'w'
```




## fstring

```python
words = ['sky', 'war', 'cup', 'eleven', 'culminate']

for word in words:
    print(f'{word} has {len(word)} latin characters')
```


## type function

```python
def f():
    pass

data = [1, 2, 3, 4, 'falcon', 3.4, 5.5, True, False, f]

for e in data:
    # if type(e) == int or type(e) == float:
    #     print(e)

    if type(e) in (int, float):
        print(e)
```

```python
def f():
    pass

data = ['war', 'water', 1, 2, 3, 'bar', 4, 'falcon', 3.4, 5.5, True, False, 'warm', f]
w_words = []

for e in data:
    if type(e) == str and e.startswith('w'):
        w_words.append(e)

        
print(w_words)
```


```python
vals = [1, 2, 6, 8, -40, -3]
vals2 = [-4, 45, 11, -7, 11, 0, 18]

mysum = 0

for e in vals:
    mysum += e

for e in vals2:
    mysum += e

print(mysum)
print(sum(vals + vals2))
```

## sum values of vals and vals2

```python
data = '1-2-3-4-5-6-7-8-9-10'

res = data.split('-')
print(res)

mysum = 0

for e in res:
    mysum += int(e)

print(mysum)
```

## calculate sum of numbers

## sum of values in file

```python
filename = 'vals.txt'

mysum = 0

with open(filename, 'r') as f:

    lines = f.readlines()

    for line in lines:
        mysum += int(line.strip())

    print(mysum)
```
