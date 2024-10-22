# Priklady

## Filter words

```python
import requests


def is_w_r(word):

    return word.startswith(('w', 'W', 'r', 'R'))

    # if (
    #     word.startswith("w")
    #     or word.startswith("W")
    #     or word.startswith("r")
    #     or word.startswith("R")
    # ):
    #     return True
    # else:
    #     return False


url = "https://raw.githubusercontent.com/janbodnar/Python-Skolenie/refs/heads/master/data/unix-words.txt"

resp = requests.get(url)
content = resp.content.decode("utf8")

lines = content.splitlines()

words_w_r = tuple(filter(is_w_r, lines))

print(len(words_w_r))
print(words_w_r[:30])
```


```python
words = ["small,", "sky\t\t", "\ntomorrow", "like?  ", "\nalias", "war.", ",water"]
```

```python
words = ["small,", "sky\t\t", "\ntomorrow", "like?  ", "\nalias", "war.", ",water"]

words_cleaned = []

for word in words:
    if '.' in word:
        word = word.replace('.', '')
    if ',' in word:
        word = word.replace(',', '')
    if '?' in word:
        word = word.replace('?', '')

    words_cleaned.append(word.strip())

print(words_cleaned)
```

---

```python
words = ["small,", "sky\t\t", "\ntomorrow", "like?  ", "\nalias", "war.", ",water"]

def clean_data(word):
    if '.' in word:
        word = word.replace('.', '')
    if ',' in word:
        word = word.replace(',', '')
    if '?' in word:
        word = word.replace('?', '')

    return word.strip()


words_cleaned = tuple(map(clean_data, words))
print(words_cleaned)
```

---

```python
import re

words = ["small,", "sky\t\t", "\ntomorrow", "like?  ", "\nalias", "war.", ",water", "great!", ";tall"]

def clean_data(word):

    pattern = re.compile(r'[,;?.!;\s]')
    word = re.sub(pattern, '', word)

    return word


words_cleaned = tuple(map(clean_data, words))
print(words_cleaned)
```



## Read CSV data

```python
from collections import namedtuple

User = namedtuple("User", "first_name last_name city")

file_name = "users.csv"

users = []

with open(file_name, "r") as f:

    for line in f:
        fields = line.split(";")
        u = User(fields[0], fields[1], fields[2].rstrip())

        users.append(u)

user_last_name_w = tuple(filter(lambda user: user.last_name.startswith("W"), users))
print(len(user_last_name_w))

for user in user_last_name_w[0:21]:
    print(user)
```

---

```python
from collections import namedtuple

User = namedtuple("User", "first_name last_name city")

file_name = "users.csv"

users = []

with open(file_name, "r") as f:

    for line in f:
        fields = line.split(";")
        u = User(fields[0], fields[1], fields[2].rstrip())

        users.append(u)

user_last_name_w = tuple(filter(lambda user: user.last_name.startswith("W"), users))

file_name2 = 'users_w.csv'

with open(file_name2, 'w') as f:

    for user in user_last_name_w:
        row = f'{user.first_name},{user.last_name},{user.city}\n'
        f.write(row)
```



## generate fake data

```python
from faker import Faker

faker = Faker()

file_name = 'users.csv'

with open(file_name, 'w') as f:

    for _ in range(1000):

        first_name = faker.first_name()
        last_name = faker.last_name()
        city = faker.city()

        user = f'{first_name},{last_name},{city}\n'
        f.write(user)
```



## namedtuple

```python
from collections import namedtuple


User = namedtuple('User', 'first_name last_name occupation')

u1 = User('John', 'Doe', 'gardener')
print(u1)
print(u1.first_name)
print(u1.last_name)
print(u1.occupation)

u2 = User('Roger', 'Roe', 'driver')
print(u2)
print(u2.first_name)
print(u2.last_name)
print(u2.occupation)
```


## Filer/map

```python
vals = [1, 2, 3, -2, 0, -3, -1, 9]

positive = tuple(filter(lambda e: e > 0, vals))
print(positive)

negative = tuple(filter(lambda e: e < 0, vals))
print(negative)

words = ['sky', 'war', 'water', 'cup', 'cloud', 'ten', 'forest']

words_c_w = tuple(filter(lambda e: e.startswith('w') or e.startswith('c'), words))
print(words_c_w)
```


## Parse words

```python

import requests

url = 'https://webcode.me/thermopylae.txt'

resp = requests.get(url)
content = resp.content.decode('utf8')

words = content.split(' ')
words_cleaned = []

for word in words:

    if '.' in word: 
         word = word.replace('.', '')

    if ',' in word: 
         word = word.replace(',', '')
       
    words_cleaned.append(word.strip())


words_2 = []

for word in words_cleaned:
     if len(word) == 2:
          words_2.append(word)

print(words_2)
print(set(words_2))
```


## Download image

```python

import requests

url = 'https://static.wikia.nocookie.net/theiceage/images/4/4a/SIdSloth2.jpg'

resp = requests.get(url)
img_data = resp.content

file_name = 'sid_image.jpg'

with open(file_name, 'wb') as f:

    f.write(img_data)
```

## Show image in UI

```python
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def display_image_from_url(url):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))

    root = tk.Tk()
    root.title("Image from URL")

    tk_image = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_image)
    label.pack()

    root.mainloop()

# Replace 'YOUR_IMAGE_URL' with the actual URL of the image you want to display
display_image_from_url('https://static.wikia.nocookie.net/theiceage/images/4/4a/SIdSloth2.jpg')
```

## Show image in web app

```python
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_image():

    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Display Image</title>
    </head>
    <body>
        <h1>Image from URL</h1>
        <img src='https://static.wikia.nocookie.net/theiceage/images/4/4a/SIdSloth2.jpg'>
    </body>
    </html>
    '''

    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
```



## Filter by type

```python
vals = [1, 2, 4, 'falcon', 'war', 3.4, 2.3, True, False, None, (1, 2, 3), (3, 4)]

for val in vals:
    if type(val) == int:
        print(val)
```


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
