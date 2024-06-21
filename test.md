# Code examples 

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
