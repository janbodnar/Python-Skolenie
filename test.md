# Priklady

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
