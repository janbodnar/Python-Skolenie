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
