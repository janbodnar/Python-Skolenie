# Test example


```python
words = ['sky', 'blue', 'rock', 'pen', 'cup']

print(len(words))

print(words[0])
print(words[-1])
print(words[4])

for word in words:
    print(word, end=" ")

words.sort()

print()

for word in words:
    print(word, end=" ")
```



```python
myname = 'John Doe'
age = 34

print(f"{myname} is {age} years old")
```



## Datetime

```python
#!/usr/bin/python

import datetime

now = datetime.datetime.now()
print(now)

d = datetime.date.today()
print(d)

t = datetime.datetime.now().time()
print(t)
```


```python

vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# while cyklus
# mysum - vysledna sume
# i - pomocna premenna
# len - zisti velkost ntice
```


```python
n_oranges = 12
n_apples = 23

print('There are %d oranges and %d apples in the basket' % (n_oranges, n_apples))
print('There are {0} oranges and {1} apples in the basket'.format(n_oranges, n_apples))
print(f'There are {n_oranges} oranges and {n_apples} apples in the basket')
```

```python

nums = "1,5,6,8,2,3,1,9"

k = nums.split(",")
print(k)

mysum = 0

for e in k:
    mysum = mysum + int(e)

print(e)
```
