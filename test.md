# Priklady

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
