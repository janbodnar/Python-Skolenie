# Priklady

## splitlines

```python
data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

lines = data.splitlines()
lines.pop(0)

mysum = 0

for line in lines:
    fields = line.split(',')
    
    for field in fields:
        mysum += int(field)

print(mysum)
```

## StringIO

```python
from io import StringIO

# calculate sum
data = '''
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
'''

# with open('words.txt', 'r') as f:
#    lines = f.readlines()


fdata = StringIO(data)

lines = fdata.readlines()
lines.pop(0)

lines = [line.strip() for line in lines]

mysum = 0

for line in lines:
    fields = line.split(',')
    
    for field in fields:
        mysum += int(field)

print(mysum)
```


