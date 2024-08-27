# Priklady

## Count vowels, consonants, whitespace

```python

vowels = 0
consonants = 0
punctuations = 0
whitespace = 0
unknown = 0

file_name = 'thermopylae.txt'

with open(file_name) as f:

    contents = f.read()

    for c in contents:
        if c in 'aeiouAEIOU':
            vowels += 1
        elif c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            consonants += 1
        elif c in '.!,:,?':
            punctuations += 1
        elif c in ' \n\t':
            whitespace += 1
        else:
            unknown += 1


print(f'vowels: {vowels}')
print(f'consonants: {consonants}')
print(f'whitespace: {whitespace}')
print(f'punctuations: {punctuations}')
print(f'unknown: {unknown}')
```

---

```python
import string

ascii = 0
punctuations = 0
whitespace = 0
unknown = 0

file_name = 'thermopylae.txt'

with open(file_name) as f:

    contents = f.read()

    for c in contents:
        if c in string.ascii_letters:
            ascii += 1
        elif c in string.punctuation:
            punctuations += 1
        elif c in string.whitespace:
            whitespace += 1
        else:
            unknown += 1


print(f'ascii: {ascii}')
print(f'whitespace: {whitespace}')
print(f'punctuations: {punctuations}')
print(f'unknown: {unknown}')
```


## Count number of characters in file

```python
letters = {}

file_name = 'thermopylae.txt'

with open(file_name) as f:

    contents = f.read()

    for c in contents:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

print(letters)

print(f'The letter a is present {letters['a']} times')
```
