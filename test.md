# Priklady


```python
# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

# print data using fstring
data2 = """John,Doe,gardener
Roger,Roe,driver
Paul,Smith,teacher
"""

# read words.txt file
# print words starting with w or c
```

Riesenie: 

```python
# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

mysum = 0

fields = data.split(",")
# print(fields)

for field in fields:
    mysum += int(field)

print(mysum)


# print data using fstring
data2 = """John,Doe,gardener
Roger,Roe,driver
Paul,Smith,teacher
"""

lines = data2.splitlines()
# print(lines)

for line in lines:
    fields = line.split(",")
    print(f'{fields[0]} {fields[1]} is a {fields[2]}')


file_name = 'words.txt'

with open(file_name, 'r') as f:

    for line in f:
        if line.startswith('w') or line.startswith('c'):
            print(line.strip())
```
