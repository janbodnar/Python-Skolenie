# Priklady



## Opakovanie

```python

first_name = 'John'
last_name = 'Doe'
occupation = 'gardener'
age = 23

msg = f'{first_name} {last_name} is a {occupation} and he is {age} years old'
print(msg)


words = ['sky', 'try', 'wrong', 'pen', 'cloud', 'atom', 'war', 'water', 'cup']
# print first, fourth, last element, one but last
# print all words in uppercase
# print words starting with w, ending with y

print(words[0], words[3], words[-1], words[-2])

for word in words:
    print(word.upper())

for word in words:
    if word.startswith('w'):
        print(word)

for word in words:
    if word.endswith('y'):
        print(word)



# word = 'falcon'
# # print length
# # print first, last letter
#
#
# vals = [1, 2, 3, 4, 5, 6, 7, 8]
# # calculate sum
# # calculate sum of even values
#
# data = ['1', '2', '3', '4', '5', '6', '7', '8']
# # calculate sum of values

```



## startswith/endswith

```python
words = ['sky', 'wrong', 'pen', 'cloud', 'atom', 'war', 'water', 'cup']

for word in words:
    if word.startswith('w') or word.startswith('c'):
        print(word)

for word in words:
    msg = f'{word} has {len(word)} letters'
    print(msg)
```

## Casting

```python
name = "John Doe"
age = 34
occupation = 'gardener'

msg = name + " is " + str(age) + " years old"
msg2 = f"{name} is {age} years old and he is a {occupation}"

print(msg)
print(msg2)

n1 = '11'
n2 = '34'

print(int(n1) + int(n2))
```

## For cyklus

```python
lyrics = '''
Are you really here or am I dreaming
I can't tell dreams from truth
for it's been so long since I have seen you
I can hardly remember your face anymore
'''

# print(lyrics)

for letter in lyrics:

    if letter not in 'auioye':
        print(letter, end=" ")


    # if letter == 'a':
    #     print(letter, end=" ")
    # elif letter == 'e':
    #     print(letter, end=" ")
    # elif letter == 'i':
    #     print(letter, end=" ")
    # elif letter == 'o':
    #     print(letter, end=" ")
    # elif letter == 'u':
    #     print(letter, end=" ")
```

## Neparne cisla

```python
vals = [1, 2, 3, 4, 5, 6, 7, 8]

for val in vals:
    if val % 2 == 1:
        print(val)

    # if val % 2 != 0:
    #     print(val)
```
