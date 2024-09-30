# Priklady 

## Zaver

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
