# Lambda functions

Python lambda functions, also known as anonymous functions, are inline functions  
that do not have a name. They are created with the lambda keyword. 

Python lambda functions are restricted to a single expression. They can be used  
wherever normal functions can be used.

Python lambda has the following syntax:

    z = lambda x: x * y

The statement creates an anonymous function with the lambda keyword. The function  
multiplies two values. The x is a parameter that is passed to the lambda function.  
The parameter is followed by a colon character. The code next to the colon is  
the expression that is executed when the lambda function is called.  
The lambda function is assigned to the z variable.

## Lambda & map 

```python
#!/usr/bin/python

nums = [1, 2, 3, 4, 5, 6]

nums_squared = map(lambda e: e * e, nums)

for num in nums_squared:
    print(num)
```

## Lambda & min/max

```python
#!/usr/bin/python

from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    name: str
    price: int

cars = [
    Car("Audi", 52642), Car("Mercedes", 57127), Car("Skoda", 9000),
    Car("Volvo", 29000), Car("Bentley", 350000), Car("Citroen", 21000),
    Car("Hummer", 41400), Car("Volkswagen", 21601)
]

n = min(cars, key=lambda c: c.price)
print(n)

n = max(cars, key=lambda c: c.price)
print(n)
```

## Lambda & filter 

```python
#!/usr/bin/python

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

res = filter(lambda e: e % 2, vals)
print(list(res))
```

---

```python
#!/usr/bin/python

from products import get_products

data = get_products()

res = filter(lambda p: p.category == 'Beverages' and p.units_in_stock > 100, data)

for p in res:
    print(p)
```

## Lambda & sort 

```python
#!/usr/bin/python

users = [
  {'name': 'John Doe', 'date_of_birth': 1987},
  {'name': 'Jane Doe', 'date_of_birth': 1996},
  {'name': 'Robert Brown', 'date_of_birth': 1977},
  {'name': 'Lucia Smith', 'date_of_birth': 2002},
  {'name': 'Patrick Dempsey', 'date_of_birth': 1994}
]

users.sort(reverse=True, key=lambda e: e['date_of_birth'])

for user in users:
    print(user)
```
---

```python
#!/usr/bin/python

from products import get_products

data = get_products()
data.sort(key=lambda e: e.product_name, reverse=True)

for p in data:
    print(p)
```

## Lambda & groupby

```python
#!/usr/bin/python

from itertools import groupby

words = ['key', 'water', 'war', 'rock', 'cup', 'cloud', 'matter', 'wood',
         'forest', 'falcon', 'foam', 'wry', 'wrath', 'up', 'auto', 'roast',
         'cool', 'computer']
words.sort()

res = [(k, list(g)) for k, g in groupby(words, key=lambda e: e[0])]

for k, g in res:
    print(f'{k}: {g} -> {len(g)}')
```

## Lambda & Tkinter

```python
#!/usr/bin/python

from tkinter import Tk, BOTH, messagebox
from tkinter.ttk import Frame, Button


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()


    def initUI(self):

        self.parent.title("Buttons")

        self.pack(fill=BOTH, expand=1)

        btn1 = Button(self, text="Button 1",
            command=lambda: self.onClick("Button 1"))
        btn1.pack(padx=5, pady=5)

        btn2 = Button(self, text="Button 2",
            command=lambda: self.onClick("Button 2"))
        btn2.pack(padx=5, pady=5)

        btn2 = Button(self, text="Button 3",
            command=lambda: self.onClick("Button 3"))
        btn2.pack(padx=5, pady=5)


    def onClick(self, text):

        messagebox.showinfo("Button label", text);


def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
```


