# Opakovanie

## Rectangle

```python
import sys

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def area(self):

        return self.width * self.height


# print(sys.argv)


width = sys.argv[1]
height = sys.argv[2]


r = Rectangle(int(width), int(height))
print(r.area())
print(r.get_width(), r.get_height())

r.set_height(40)
print(r.area())
```



```python
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def area(self):

        return self.width * self.height

w = input("Enter width:")
h = input("Enter height:")

r = Rectangle(int(w), int(h))
print(r.area())
print(r.get_width(), r.get_height())

r.set_height(40)
print(r.area())
```



## Objects

```python


class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 4)
mercy = Cat('Mercy', 1)

print(missy.name, missy.age)
print(lucky.name, lucky.age)
print(mercy.name, mercy.age)

# procedural style:

# cat_name1 = 'Missy'
# cat_age1 = 3
# 
# cat_name2 = 'Lucky'
# cat_age2 = 4
# 
# cat_name3 = 'Mercy'
# cat_age3 = 1
```







The `words.txt` file:

```
smart
war
abyss
ocean
park
water
ram
new
cup
pen
dog
cat
chair
```

```python
# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

# using a list comprehension, generate a list of random values
# between 1 .. 100. 

# calculate sum
data = "1;2;3;4;5;6,7;8;9;10"

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']

# read words.txt into a list and sort it
```

## Riesenia

```python
# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

words2 = [word.lower() for word in words]
print(words2)

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

evens = [val for val in vals if val % 2 == 0]
print(evens)

# using a list comprehension, generate a list of 100 random values
# between 1 .. 100. 
import random

randvals = [random.randint(1, 101) for _ in range(100)]
print(randvals)

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']
# words3 = [word for word in words2 if len(word) == 3 and word.endswith('t')]
words3 = [word for word in words2 if len(word) == 3 and word[-1] == 't']

print(words3)

# read words.txt into a list and sort it
filename = 'words.txt'
with open(filename, 'r') as fd:

    lines = fd.readlines()
    lines_cleaned = [line.strip() for line in lines]

    print(lines_cleaned)

# calculate sum
data = "1;2;3;4;5;6,7;8;9;10"

data2 = data.replace(',', ';')
print(data2)

fields = data2.split(';')
print(fields)

print(sum(int(field) for field in fields))

# vals = [int(field) for field in fields]
# print(vals)
# 
# print(sum(vals))
```



