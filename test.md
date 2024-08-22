# Priklady

```python
vals = [1, 2, 6, 8, -40, -3]
vals2 = [-4, 45, 11, -7, 11, 0, 18]

mysum = 0

for e in vals:
    mysum += e

for e in vals2:
    mysum += e

print(mysum)
print(sum(vals + vals2))
```

## sum values of vals and vals2

```python
data = '1-2-3-4-5-6-7-8-9-10'

res = data.split('-')
print(res)

mysum = 0

for e in res:
    mysum += int(e)

print(mysum)
```

## calculate sum of numbers

## sum of values in file

```python
filename = 'vals.txt'

mysum = 0

with open(filename, 'r') as f:

    lines = f.readlines()

    for line in lines:
        mysum += int(line.strip())

    print(mysum)
```
