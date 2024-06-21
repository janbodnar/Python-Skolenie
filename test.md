# Code examples 




## Lambda function

```python
words = ['sky', 'cup', 'war', 'water', 'cloud', 'atom', 'first']

res = list(filter(lambda word:word[0] in ['w', 'c'], words))
print(res)


vals = [-2, 0, 1, -9, 4, 5, 2, -4]

positive = list(filter(lambda e: e > 0, vals))
print(positive)

negative = list(filter(lambda e: e< 0, vals))
print(negative)
```

## map fun 

```python
words = ['sky', 'cup', 'war', 'water', 'cloud', 'atom', 'first']

res = list(map(lambda word: word.upper(), words))
print(res)


vals = [-2, 0, 1, -9, 4, 5, 2, -4]

twice = list(map(lambda e: e * 2, vals))
print(twice)
```


## filter fun

```python
def is_w_c(word):
    return word[0] in ['w', 'c']

words = ['sky', 'cup', 'war', 'water', 'cloud', 'atom', 'first']

res = list(filter(is_w_c, words))
print(res)
```

---

```python
def is_positive(e):
    return e > 0

def is_negative(e):
    return e < 0

print(is_negative(3))

vals = [-2, 0, 1, -9, 4, 5, 2, -4]

positive = list(filter(is_positive, vals))
print(positive)

negative = list(filter(is_negative, vals))
print(negative)
```


## Reading words

```python
fname = "words.txt"
w_c_words = []

with open(fname, 'r') as f:
    lines = f.readlines()
    for word in lines:
        cleaned_word = word.rstrip()
        if cleaned_word.startswith('w') or cleaned_word.startswith('c'):
            w_c_words.append(cleaned_word)

print(w_c_words)
```


## Writing to files 

```python
words = ['falcon', 'forest']
fname = "words.txt"

with open(fname, 'a') as f:

    for word in words:
        f.write(word + '\n')
```


## Word frequency

```python
def create_word_frequency(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    return word_freq

# Usage
file_path = 'thermopylae.txt'  # replace with your file path
word_frequency = create_word_frequency(file_path)
print(word_frequency)
```


## Recap

```python
users = [("John Doe", "gardener"), ("Roger Roe", "driver"), ("Paul Novak", "teacher")]
# John Doe is a gardener/ for loop/fstring/[]

for user in users:
    print(f'{user[0]} is a(n) {user[1]}')
```

```python
words = ["sky", "cup", "war", "water", "warm", "cloud", "atom"]
all = 0
w_or_c = 0

print(words)

for word in words:
    all += len(word)

    # if word[0] in ("w", "c"):
    if word.startswith("w") or word.startswith("c"):
        w_or_c += len(word)

print(f'there are {all} ascii characters')
print(f'there are {w_or_c} ascii characters in words starting with w or c')
```


## nested tuples

```python
mix = (1, 2, "solaris", (1, 2, 3, (4, 5, 6)))

print(mix[3][3][0])
print(mix[3][3][1])
print(mix[3][3][2])
```

## startswith

```python
words = ['war', 'cup', 'cloud', 'atom', 'water', 'key']

for word in words:
    # if word.startswith('w,') or word.startswith('c'):
    if word[0] in ['w', 'c']:
        print(word)

# words = ['war', 'cup', 'cloud', 'atom', 'water', 'key']
#
# pattern = re.compile(r'^[cw].*')
#
# for word in words:
#     if re.fullmatch(pattern, word):
#         print(word)
```


## Split & count chars

```python
# split sentence
# word has n characters split/len/fstring/for loop
msg = "There is an old falcon in the sky"

words = msg.split(' ')
print(words)

for word in words:
    print(f'{word} has {len(word)} ascii characters')
```

## Splitting

```python
s = " Eagle  "

s2 = s.rstrip()
s3 = s.lstrip()
s4 = s.strip()

print(f'{s} {len(s)}')
print(f'{s2} {len(s2)}')
print(f'{s3} {len(s3)}')
print(f'{s4} {len(s4)}')
```
