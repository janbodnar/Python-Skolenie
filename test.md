# Priklady

```python
file_name = 'words.txt'

with open(file_name) as f:

    lines = f.readlines()

    for word in lines:
        print(f'{word.rstrip()} has {len(word.rstrip())} characters')
```

```python
# first_name = 'John'
# last_name = 'Doe'
# occupation = 'gardener'

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
occupation = input("Enter your occupation: ")


# msg = first_name + ' ' + last_name + " is a " + occupation
msg = f'User {first_name} {last_name} is a {occupation}'

print(msg)
```


```python
file_name = 'words.txt'

with open(file_name) as f:

    lines = f.readlines()
    # print(lines)

    for line in lines:

        if line.startswith('w') or line.startswith('c') :
            print(line.rstrip())
```


```python
nums = "1,5,6,8,2,3,1,9"
fields = nums.split(",")

mysum = 0

for field in fields:
    mysum += int(field)

print(mysum)
```


```python
name = 'Peter'
age = 23
occupation = 'programmer'

print('%s is %d years old and he is a %s' % (name, age, occupation))
print('{} is {} years old and he is a {}'.format(name, age, occupation))
print(f'{name} is {age} years old and he is a {occupation}')
```


```python
word = 'falcon'

i = 1

while i <= 10:

    print(f'{i}. {word}')
    i = i + 1

print('end of program')
```


```python
# vals = [1, 2, 2, 3, 3, 4, 5, 6]
#
# print(vals)
# print(vals[0])
# print(vals[1])
# print(vals[3])
# print(vals[7])
#
# print(vals[-1])
# print(vals[-2])

words = ['sky', 'atom', 'new', 'war', 'cloud', 'pen']

print(words[0])
print(words[-1])
print(len(words))
# print(sum(words))
```

```python
name = "John Doe"
age = 23
occupation = 'gardener'

print(name, age, occupation)

print(type(name))
print(type(age))
```


```python
vals = [1, 2, 2, 3, 3, 4, 5, 6]

print(vals)
print(sum(vals))
print(len(vals))
print(len(occupation))
```
