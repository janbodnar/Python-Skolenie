# Priklady 


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
