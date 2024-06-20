# Code examples 

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
