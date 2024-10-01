# Priklady 


## Pouzitie CSV modulu

```python
import csv

mysum = 0
file_name = 'data.csv'

with open(file_name) as f:

    reader = csv.reader(f)

    for fields in reader:

        for field in fields:
            mysum += int(field)

print(mysum)
```


## Nacitanie dat zo CSV suboru

Plus vypocitanie sumy

```python
mysum = 0

file_name = 'data.csv'

with open(file_name) as f:

    lines = f.readlines()

    for line in lines:

        row = line.rstrip()
        fields = row.split(",")

        for field in fields:
            mysum += int(field)

print(mysum)
```


## Vypisanie suboru s diakritikou

```python
file_name = 'newfile.txt'

with open(file_name, 'r', encoding="utf8") as f:

    for line in f:
        print(line.rstrip())
```


## Vypisanie suboru z disku

```python
file_name = 'C:/Users/bodnar/Documents/words2.txt'

with open(file_name, 'r') as f:

    for line in f:
        print(line.rstrip())
```


## Opakovanie

```python

mysum = 0

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in vals:
    mysum = mysum + val

print(mysum)

print('----------------------------')

# calculate sum using for loop

words = ['sky', 'word', 'soup', 'cloud', 'cup', 'town', 'war', 'sad', 'water']

for word in words:
    if word.startswith('w'):
        print(word, end=' ')

print()

for word in words:
    if word.startswith('w') or word.startswith('c'):
        print(word, end=' ')

print('\n----------------------------')

file_name = 'words.txt'

with open(file_name, 'r') as f:

    for line in f:
        if line.startswith('w'):
            print(line.rstrip())


# print words starting with 'w'
# print words starting with 'w' or 'c'

# print words starting with 'w' from file words.txt
```



## Zaver


```python
name = "John Doe"
age = 23
occupation = 'gardener'

# fstring

msg = f'{name} is {age} years old, he is a {occupation}'
print(msg)

# suma
# spocitaj kladne cisla

vals = [1, 2, 3, -4, -5, 6, 7, 8, -9, 10]
print(sum(vals))

sum_pos = 0

for val in vals:
    if val > 0:
        sum_pos += val

print(sum_pos)

# spocitaj vsetky znaky
# spocitaj znaky slov zacinajuce na w

all_chars = 0
w_chars = 0

words = ['sky', 'water', 'sun', 'black', 'town', 'water']

for word in words:
    all_chars += len(word)

print(all_chars)

for word in words:
    if word.startswith('w'):
        w_chars += len(word)

print(all_chars)
print(w_chars)
```



```python
name = "John Doe"
age = 23
occupation = 'gardener'

# fstring

vals = [1, 2, 3, -4, -5, 6, 7, 8, -9, 10]
# suma
# spocitaj kladne cisla

words = ['sky', 'water', 'sun', 'black', 'town', 'water']
# spocitaj vsetky znaky
# spocitaj znaky slov zacinajuce na w
```





## Letter types

```python
import string

sentence = "There are 22 apples. We live now in 2024. Huraa!"

alphas = 0
digits = 0
spaces = 0
puncts = 0


for i in sentence:

   if i.isalpha():
      alphas = alphas + 1

   elif i.isdigit():
      digits += 1

   elif i.isspace():
      spaces += 1

   elif i in string.punctuation:
       puncts += 1

print("There are", len(sentence), "characters")
print("There are", alphas, "alphabetic characters")
print("There are", digits, "digits")
print("There are", spaces, "spaces")
print("There are", puncts, "punctuation characters")
```


## Sum of values

```python
nums = "1,5,6,8,2,3,1,9"

fields = nums.split(",")
print(fields)

mysum = 0

for val in fields:
    mysum = mysum + int(val)
```

## Formatting

```python
#!/usr/bin/python

name = 'Peter'
age = 23
occupation = 'programmer'

print('%s is %d years old and he is a %s' % (name, age, occupation))
print('{} is {} years old and he is a {}'.format(name, age, occupation))
print(f'{name} is {age} years old and he is a {occupation}')
```
