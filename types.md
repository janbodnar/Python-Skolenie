# Types

## Check types

```python
#!/usr/bin/python

class Being:
    pass


objects = [1, -2, 3.4, None, False, [1, 2], "Python", (2, 3), Being(), {}]

for e in objects:
    match e:
        case None:
            print(f'{e} is a null value')
        case list():
            print(f'{e} is a list cointainer')
        case tuple():
            print(f'{e} is a tuple cointainer')
        case True | False:
            print(f'{e} is a boolean value')
        case float():
            print(f'{e} is a float')
        case _val if isinstance(_val, dict):
            print(f'{e} is a dictionary')
        case _val if isinstance(_val, int):
            print(f'{e} is an integer')
```
