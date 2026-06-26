# Priklady



## map function

```python
vals = [1, 2, 3, 4, 5]


def twice(e):
    return 2 * e

def cube(e):
    return e * e * e

vals_2 = list(map(twice, vals))
print(vals_2)

vals_3 = list(map(cube, vals))
print(vals_3)
```

## filter function with lambda

```python
vals = [2, -3, 4, 9, 0, 1, -2, -4]

positive_values = list(filter(lambda e: e > 0, vals))
print(positive_values)

negative_values = list(filter(lambda e: e < 0 , vals))
print(negative_values)
```


## filter function

```python
def is_positive(e):
    return e > 0

def is_negative(e):
    return e < 0

vals = [2, -3, 4, 9, 0, 1, -2, -4]

positive_values = list(filter(is_positive, vals))
print(positive_values)

negative_values = list(filter(is_negative, vals))
print(negative_values)
```


## unnamed variable

```python
word = 'falcon'

for _ in range(1, 8):
    print(word)
```


## Column selection

```
first name   last name      occupation         
John         Doe            gardener           
Roger        Roe            driver             
Paul         Novak          teacher            
Jane         Smith          accountant         
Lucia        Dorak          programmer         
Robert       Williams       soldier            
```

Shift + Alt + Mouse drag  
Ctrl + Shift + Alt + Cursor keys  



## rich table

```python
"""Simple demonstration of the rich library — creating a table."""

from rich.console import Console
from rich.table import Table
from rich import print as rprint

# ── Quick preview: rich print ──
rprint("\n[bold cyan]📦 rich[/] [green]library demo[/]\n")

# ── Create a table ──
table = Table(title="📊 Monthly Sales Report", title_style="bold magenta")

# Define columns
table.add_column("Month", style="cyan", no_wrap=True)
table.add_column("Revenue", justify="right", style="green")
table.add_column("Expenses", justify="right", style="red")
table.add_column("Profit", justify="right", style="bold yellow")
table.add_column("Status", justify="center")

# Add rows
table.add_row("January",  "$45,200", "$32,100", "$13,100", "✅")
table.add_row("February", "$42,800", "$30,500", "$12,300", "✅")
table.add_row("March",    "$51,300", "$35,200", "$16,100", "✅")
table.add_row("April",    "$38,900", "$31,800",  "$7,100", "⚠️")
table.add_row("May",      "$47,600", "$30,100", "$17,500", "✅")
table.add_row("June",     "$55,000", "$36,400", "$18,600", "✅")
table.add_row("July",     "$41,200", "$33,700",  "$7,500", "⚠️")
table.add_row("August",   "$49,800", "$32,900", "$16,900", "✅")
table.add_row("September","$53,400", "$34,600", "$18,800", "✅")
table.add_row("October",  "$48,100", "$31,200", "$16,900", "✅")
table.add_row("November", "$56,700", "$37,800", "$18,900", "✅")
table.add_row("December", "$62,300", "$40,100", "$22,200", "✅")

# Add a separator row (footer summary)
table.add_section()
table.add_row(
    "[bold]Total[/]",
    "[bold]$592,300[/]",
    "[bold]$406,400[/]",
    "[bold]$185,900[/]",
    "[bold]🟢[/]",
    end_section=True,
)

# Render the table
console = Console()
console.print(table, justify="center")

# ── Bonus: styled summary panel ──
from rich.panel import Panel
from rich.text import Text

summary = Text()
summary.append("\nTotal Revenue:  ", style="white")
summary.append("$592,300\n", style="bold green")
summary.append("Total Expenses: ", style="white")
summary.append("$406,400\n", style="bold red")
summary.append("Net Profit:     ", style="white")
summary.append("$185,900\n", style="bold yellow")
summary.append("Profit Margin:  ", style="white")
summary.append("31.4%\n", style="bold cyan")

panel = Panel(
    summary,
    title="[bold magenta]📈 Summary[/]",
    border_style="blue",
    padding=(1, 4),
)
console.print(panel, justify="center")

rprint("\n[dim]✨ Built with [link=https://rich.readthedocs.io/]rich[/][/]\n")
```



## fstring fun

```python
def cube(x):
    return x * x * x

n = 10

print(f'{n} cubed is: {cube(n)}')
```


## Opakovanie 

```python
# spocitaj pocet pismen
words = ['sky', 'power', 'auto', 'small', 'car', 'tea', 'cup']

# spocitaj cisla
vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# spocitaj cisla
data = '1,2,3,4,5,6,7,8,9,10'

# vyber nahodne 3 cisla
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# nahodnym sposobom preusporiadaj cisla
vals2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
```


## Riesenia

```python
# spocitaj pocet pismen
words = ['sky', 'power', 'auto', 'small', 'car', 'tea', 'cup']

count = 0
for word in words:
    count += len(word)

print(f'# of characters: {count}')


# spocitaj cisla
vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

suma = 0
for val in vals:
    suma += int(val)

print(suma)


# spocitaj cisla
data = '1,2,3,4,5,6,7,8,9,10'
parts = data.split(',')
print(parts)

suma = 0
for part in parts:
    suma += int(part)

print(suma)


# vyber nahodne 3 cisla
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

three_random_vals = random.sample(vals, 3)
print(three_random_vals)

import random


# nahodnym sposobom preusporiadaj cisla
vals2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
vals3 = list(vals2)

random.shuffle(vals3)
print(vals3)
```

https://docs.google.com/document/d/1K81CLCzao6z_S242dqPF8dHgHFv4g31J7EQ1PYBg9aY/edit?usp=drive_link

## random funtions

```python
import random

# print(dir(random))

vals = [1, 2, 3, 4, 5]
print(vals)
random.shuffle(vals)
print(vals)

words = ['sky', 'tower', 'small', 'blue', 'cup']
random_word = random.choice(words)
print(random_word)

random_words = random.sample(words, 3)
print(random_words)
```




## name clash

```python
suma = 0
vals = (1, 2, 3, 4, 5)

for val in vals:
    suma += val

print(suma)


print(sum(vals))
```

## Bar chart

```python
import matplotlib.pyplot as plt

# Sample data
categories = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
sales = [120, 90, 150, 70, 110]
colors = ["#FF6B6B", "#FFD93D", "#FF8C94", "#6BCB77", "#4D96FF"]

# Create the bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, sales, color=colors, edgecolor="white", linewidth=1.5)

# Add value labels on top of each bar
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        str(bar.get_height()),
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
    )

# Labels and title
plt.xlabel("Fruit", fontsize=12)
plt.ylabel("Sales (units)", fontsize=12)
plt.title("Fruit Sales by Category", fontsize=14, fontweight="bold", pad=15)

# Remove top and right spines for a cleaner look
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# Grid for readability
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
# plt.show()

plt.savefig('barchart.png')
```



## dictionary iteration

```python
#!/usr/bin/python

data = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary", "ru": "Russia" }    

for k in data:
    print(k, data[k])

for v in data.values():
    print(v)

for k, v in data.items():
    
    print(f"{k} is an abbreviation for {v}")
```

## range function

```python
#  spocitaj cisla od 500 - 850

suma = 0

for cislo in range(500, 851):
    suma += cislo

print(suma)

print(sum(range(500, 851)))
```



## for vs while loop

```python
word = 'falcon'

for i in range(7):
    print(word)


print('-----------------------')

i = 0

while i < 7:
    print(word)

    i += 1
```


## Opakovanie

```python

# vypis 7 krat slovo falcon
word = 'falcon'

# spocitaj posledne tri hodnoty
data = [11, 22, 33, 44, 55, 66, 77, 88]

# vytvor zoznam 30 tich nahodnych 
# cisiel z rozsahu 1-100
random_vals = []

# spocitaj sumu pomocou for loopu
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# spocitaj sumu pomocou while loopu
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# spocitaj pocet samohlasok 
msg = 'and old falcon in the sky'

# spocitaj pocet slov vo vete
msg = 'There are seven falcons in the sky.'
```

Riesenia: 

```python
word = 'falcon '

print(word * 7)

i = 1 

while i <= 7:
    print(word)
    i += 1

# spocitaj posledne tri hodnoty
data = [11, 22, 33, 44, 55, 66, 77, 88]
x = data[-1]
y = data[-2]
z = data[-3]

print(x + y + z)


import random

# vytvor zoznam 30 tich nahodnych 
# cisiel z rozsahu 1-100
random_vals = []

i = 0

while i < 30:
    r = random.randint(1, 101)
    random_vals.append(r)

    i += 1

print(random_vals)

# spocitaj sumu pomocou for loopu
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

suma = 0
for val in vals:
    suma += val

print(suma)

# spocitaj sumu pomocou while loopu
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

i = 0
suma = 0

while i < len(vals):
    suma += vals[i]
    i += 1

print(suma)


# spocitaj pocet samohlasok 
msg = 'and old falcon in the sky'

count = 0

for character in msg:
    if character == 'a' or character == 'e' or character == 'e' \
        or character == 'i' or character == 'o' or character == 'u' \
        or character == 'y':
        count += 1

print(f'there are {count} vowels')

count = 0
print('----------------------------------')

for character in msg:
    if character in 'aeiouy':
        count += 1

print(f'there are {count} vowels')


# spocitaj pocet slov vo vete
msg = 'There are seven falcons in the sky.'

parts = msg.split()
print(parts)
print(len(parts))
```


## Opakovanie

```python
# napis hlasku John Doe ma 34 rokov pomocou fstringu

name = "John Doe"
age = 34

# napis slovo falcon 7 krat pomocou while loopu

# napis skript ktory zada vyzvu Enter your name a vypise Hello name!

# spocitaj sumu cisiel 1..10 pomocou while loopu
```

## Riesenia

```python
# napis hlasku John Doe ma 34 rokov pomocou fstringu

name = "John Doe"
age = 34

print(f'{name} is {age} years old')

# napis slovo falcon 7 krat pomocou while loopu
word = "falcon"
i = 0

while i < 7:

    print(word)
    i += 1

# napis skript ktory zada vyzvu Enter your name a vypise Hello name!

name = input("Enter your name: ")
print(f'Hello {name}!')

# spocitaj sumu cisiel 1..10 pomocou while loopu

i = 1
suma = 0

while i <= 10:
    suma += i
    i += 1

print(suma)
```






## Velkost retazcov

```python
s4 = "čerešňa"
print(len(s4))

s5 = "नमस्ते"
print(len(s5)) # correct is 3
```

## String formatting

```python
name = 'Peter'
age = 23
occupation = 'gardener'

# Peter is 23 years old and he is a gardener

print('%s is %d years old and he is a %s' % (name, age, occupation))
print('{} is {} years old and he is a {}'.format(name, age, occupation))
print(f'{name} is {age} years old and he is a {occupation}')
```

## not operator

```python
word = 'falcon'

character = 'f'

if character in word:
    print(f'{character} is in the word')
else:
    print(f'{character} is not in the word')

if character not in word:
    print(f'{character} is not in the word')
else:
    print(f'{character} is in the word')
```

## and operator

```python
age = 17
has_driving_licence = True

if age >= 18 and has_driving_licence == True:
    print('We can drive a car')
else:
    print('We cannot drive a car')
```


## type funkcia

```python
x = 23
print(x, type(x))

x = 'falcon'
print(x, type(x))

x = 34.5
print(x, type(x))
```

## Pretypovanie/casting

```python
x = '15'
y = '15'
print(int(x) + int(y))

n = 3
word = ' falcons'

print(str(n) + word)
```

```python
x = input("Enter a number: ")
y = input("Enter another number: ")

print('x + y is:', int(x) + int(y))
```

## input funkcia

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

msg = f'{name} is {age} years old'
print(msg)
```

## Simple fstring

```python
name = 'John Doe'
age = 34

print(name, 'is', age, 'years old')

msg = f'{name} is {age} years old'
print(msg)
```

## Znak noveho riadku

```python
x = 12

print(x, end=' ')
print(x, end=' ')
print(x, end=' ')
print(x, end=' ')

print('\nand old falcon\na stormy night\na new car')
```

## Opakovanne vykovanie kodu

```python
i = 0

msg = 'and old falcon'

while i < 5:
    print(msg)
    i = i + 1
```



```python
import random

r = random.randint(-5, 5)

print(r)

if r > 0:
    print('The r variable is positive')
elif r < 0:
    print('The r variable is negative')
else:
    print('The r variable is zero')


print('end of program')
```





















```python
import sqlite3

con = sqlite3.connect('test.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        # print(row)
        print(f'{row[0]} {row[1]} {row[2]}')
```



words.txt

```
sky
blue
small
fortune
back
alpha
current
car
belt
vase
plant
```


## Opakovanie

```python
# sum the numbers in the list and print the result
data = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# write a script that asks for use name and 
# age and then prints out a message with the name and age

# remove all the extra spaces, create a list of words
# and sorted the words in alphabetical order, print the sorted list
text = 'there\n\t are \t\t\t14 dogs    and \n\n 7 cats in the park'

# print all the even numbers from 101 to 390

# generate 250 random values between -100 and 100 
# and add them to a list, print min, max, sum of the values

# read words.txt, clean the words and sort them in 
# alphabetical in descending order, print the sorted list**


```

Riesenia

```python
# sum the numbers in the list and print the result
data = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

suma = 0

for nested in data:
    suma += sum(nested)

print(suma)

suma = sum(sum(nested) for nested in data)
print(suma)

#------------------------------------
# write a script that asks for use name and 
# age and then prints out a message with the name and age

name = input("Enter your name: ")
age = input("Enter your age: ")

msg = f"Hello {name}, you are {age} years old."
print(msg)

#------------------------------------
# remove all the extra spaces, create a list of words
# and sorted the words in alphabetical order, print the sorted list
text = 'there\n\t are \t\t\t14 dogs    and \n\n 7 cats in the park'

# riesenie 1
text2 = text.replace('\n', ' ').replace('\t', ' ')

parts = text2.split(' ')
cleaned = [part for part in parts if part != '']
print(sorted(cleaned))

# riesenie 2
text = 'there\n\t are \t\t\t14 dogs    and \n\n 7 cats in the park'
import re

parts = re.split(r'\s+', text)
print(sorted(parts))

# ------------------------------------------

# print all the even numbers from 101 to 390

for i in range(101, 390):
    if i % 2 == 0:
        print(i, end=' ')

print()

# ------------------------------------------

# generate 250 random values between -100 and 100 
# and add them to a list, print min, max, sum of the values
import random

random.seed(42)  # Set a seed for reproducibility
# 1. riesenie
rand_vals = []
for i in range(250):
    rand_vals.append(random.randint(-100, 100))

print("Min:", min(rand_vals))
print("Max:", max(rand_vals))
print("Sum:", sum(rand_vals))
print(f'first 10 values: {rand_vals[:10]}')

print('---------------------------------')

random.seed(42)  # Set a seed for reproducibility

# 2. riesenie
rand_vals = [random.randint(-100, 100) for i in range(250)]
print("Min:", min(rand_vals))
print("Max:", max(rand_vals))
print("Sum:", sum(rand_vals))
print(f'first 10 values: {rand_vals[:10]}')

# ------------------------------------------

# read words.txt, clean the words and sort them in 
# alphabetical in descending order, print the sorted list

filename = 'words.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
    # print(repr(content))
    words = content.split('\n')
    words = [word for word in words if word != '']
    words.sort(reverse=True)
    print(words)
```

https://github.com/janbodnar/AI-Skolenie  
https://www.facebook.com/profile.php?id=61590475374227

`words.txt`

```
small
up
Door
rock
Sick
war
water
Old
moat
```

## Opakovanie

```python
# calcuate sum
data = "1,2,3,4;5,6;7,8,9,10"

# filter all positive and even values
# use list comprehension
vals = (-2, -3, 0, 1, 2, 9, 0, -6, 3, 2, 8, 7)

# filter all words with 3 letters with list comprehension
words = ['sky', 'time', 'glow', 'small', 'archon', 'car', 'cup']

# clean the words, and print all that start with letter c
# use list comprehensions
words = [' sky', 'time ', ' glow', 'small\n\n', '\tarchon', ' car\r', 'cup']

# read all words from words.txt, transform into small letters 
# and sort them


```

Riesenia

```python
words = [' sky', 'time ', ' glow', 'small\n\n', '\tarchon', ' car\r', 'cup']

words_cleaned = [word.strip() for word in words]
print(words_cleaned)
words_c = [word for word in words_cleaned if word.startswith('c')]
print(words_c)

# -----------------------------------------

# read all words from words.txt, transform into small letters 
# and sort them

# absolute paths
# filename = 'C:\\Users\\Admin\\Documents\\pyprogs\\test\\words.txt'
# filename = r'C:\Users\Admin\Documents\pyprogs\test\words.txt'
# filename = 'C:/Users/Admin/Documents/pyprogs/test/words.txt'

# relative paths
filename = 'data/words.txt'

words = []

with open(filename, 'r') as file:
    
    for line in file:
        words.append(line.strip())

    print(words)
    words2 = [word.lower() for word in words]
    print(sorted(words2))

```


`https://github.com/dolph/dictionary/blob/master/unix-words`

## Sentiment analysis

DeepSeek:

```python
import json
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
)

slovak_movie_reviews = {
    1: "Príbeh bol úplne pútavý a herecké výkony brilantné. Nemohol som sa odtrhnúť ani na sekundu!",
    2: "Tempo bolo mimoriadne pomalé a postavy nemali žiadnu hĺbku. Nudil som sa už v polovici.",
    3: "Hoci vizuálne efekty boli ohromujúce, dej pôsobil predvídateľne a bez inšpirácie.",
    4: "Toto je filmové dielo, ktoré mi dojalo srdce. Každá scéna bola dokonalosť!",
    5: "Dialógy boli trápne a humor úplne zlyhal. Určite to nestojí za ten humbug.",
    6: "Bol to priemerný film – nie dobrý, ale ani úplná katastrofa. Niektoré časti ma bavili.",
    7: "Chemia medzi hlavnými postavami bola elektrizujúca a soundtrack fenomenálny!",
    8: "Film začal skvele, ale v druhej polovici sa úplne rozpadol. Veľké sklamanie.",
    9: "Vizualne ohromujúci film, ktorý dokonale spája akciu a emócie. Určite odporúčam!",
    10: "Premisa bola zaujímavá, ale realizácia bola slabá. Nedokázalo ma to zaujať."
}

reviews_text = "\n".join(f"{key}: {value}" for key, value in slovak_movie_reviews.items())

content = (
    "Rate the sentiment of each movie review on a scale of 0 to 1. "
    'Reply with a JSON object in the format {"1": 0.9, "2": 0.2, ...}. '
    "No explanation, just the JSON.\n\n"
    + reviews_text
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": content}],
    response_format={"type": "json_object"},
)

results = json.loads(response.choices[0].message.content)
for key, value in slovak_movie_reviews.items():
    print(key, results[str(key)], value)
```



Ollama: 

```python
import ollama

slovak_movie_reviews = {
    1: "Príbeh bol úplne pútavý a herecké výkony brilantné. Nemohol som sa odtrhnúť ani na sekundu!",
    2: "Tempo bolo mimoriadne pomalé a postavy nemali žiadnu hĺbku. Nudil som sa už v polovici.",
    3: "Hoci vizuálne efekty boli ohromujúce, dej pôsobil predvídateľne a bez inšpirácie.",
    4: "Toto je filmové dielo, ktoré mi dojalo srdce. Každá scéna bola dokonalosť!",
    5: "Dialógy boli trápne a humor úplne zlyhal. Určite to nestojí za ten humbug.",
    6: "Bol to priemerný film – nie dobrý, ale ani úplná katastrofa. Niektoré časti ma bavili.",
    7: "Chemia medzi hlavnými postavami bola elektrizujúca a soundtrack fenomenálny!",
    8: "Film začal skvele, ale v druhej polovici sa úplne rozpadol. Veľké sklamanie.",
    9: "Vizualne ohromujúci film, ktorý dokonale spája akciu a emócie. Určite odporúčam!",
    10: "Premisa bola zaujímavá, ale realizácia bola slabá. Nedokázalo ma to zaujať."
}

for key, value in slovak_movie_reviews.items():
    
    content = 'On the scale of 0 to 1, write the sentiment of the following movie review, use only a number:\n'
    content += value

    response = ollama.chat(
        model='granite4.1:3b',
        messages=[
            {
                'role': 'user',
                'content': content,
            }
        ],
        options={
            'temperature': 0.7,
            'top_p': 0.9,
        }
    )

    # Extract the text content from the Ollama response dictionary
    output = response['message']['content']
    print(key, value, output)
```

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    salary: int

user = User(1, 'John', 'Doe', 'john.doe@example.com', 50000)
print(user)

user2 = User(2, 'Jane', 'Smith', 'jane.smith@example.com', 60000)
print(user2)
```


```python

# calculat the number of vowels, consonants, punctuation, spaces and total
# characters in a given text.
text= """
There are three coins in a box. One of them is a two-headed coin, 
and the other two are normal coins. You pick a coin at random and flip it three
times. All three flips come up heads. What is the probability that you picked
the two-headed coin?
"""

# pick 10 random words from the list and add them to random_words list
# generate a comma-separated string of the random words and print it

# print 20 random words, withou duplicates, sorted alphabetically
words = ['sky', 'cloud', 'rain', 'sun', 'snow', 
         'wind', 'storm', 'thunder', 'lightning', 'fog', 
         'cup', 'table', 'chair', 'book', 'pen', 'phone',
         'computer', 'keyboard', 'mouse', 'monitor', 'printer', 
         'desk', 'window', 'door', 'wall', 'floor', 'ceiling', 'roof', 
         'garden', 'tree', 'flower', 'grass', 'bush', 'leaf', 
         'branch', 'root', 'fruit',
         'car', 'bus', 'train', 'plane', 'boat', 'bicycle', 'motorcycle', 
         'truck', 'subway', 'tram', 'taxi', 'ship', 'ferry',
         'dog', 'cat', 'bird', 'fish', 'hamster', 'rabbit', 'turtle', 
         'snake', 'lizard', 'frog', 'insect', 'spider', 'ant', 'bee', 
         'butterfly']
"""
```

```python
from collections import Counter
import string

text = """
There are three coins in a box. One of them is a two-headed coin, 
and the other two are normal coins. You pick a coin at random and flip it three
times. All three flips come up heads. What is the probability that you picked
the two-headed coin?
"""

vowels = set('AEIOUYaeiouy')

def categorize(char):
    if char in vowels:         return 'vowels'
    if char in string.punctuation: return 'punctuation'
    if char in string.whitespace:  return 'spaces'
    return 'consonants'

counts = Counter(categorize(c) for c in text)

print(f"Vowels:       {counts['vowels']}")
print(f"Consonants:   {counts['consonants']}")
print(f"Punctuation:  {counts['punctuation']}")
print(f"Spaces:       {counts['spaces']}")
print(f"Total:        {len(text)}")
```


```
# pick 10 random words from the list and add them to random_words list
# generate a comma-separated string of the random words and print it

# print 20 random words, withou duplicates, sorted alphabetically
words = ['sky', 'cloud', 'rain', 'sun', 'snow', 
         'wind', 'storm', 'thunder', 'lightning', 'fog', 
         'cup', 'table', 'chair', 'book', 'pen', 'phone',
         'computer', 'keyboard', 'mouse', 'monitor', 'printer', 
         'desk', 'window', 'door', 'wall', 'floor', 'ceiling', 'roof', 
         'garden', 'tree', 'flower', 'grass', 'bush', 'leaf', 
         'branch', 'root', 'fruit',
         'car', 'bus', 'train', 'plane', 'boat', 'bicycle', 'motorcycle', 
         'truck', 'subway', 'tram', 'taxi', 'ship', 'ferry',
         'dog', 'cat', 'bird', 'fish', 'hamster', 'rabbit', 'turtle', 
         'snake', 'lizard', 'frog', 'insect', 'spider', 'ant', 'bee', 
         'butterfly']



import random

begin_index = 0
end_index = len(words) - 1
random_words = []

for _ in range(10):
    random_index = random.randint(begin_index, end_index)
    random_words.append(words[random_index])

print(', '.join(random_words))
print(sorted(random_words))
```


```python
text= """
There are three coins in a box. One of them is a two-headed coin, 
and the other two are normal coins. You pick a coin at random and flip it three
times. All three flips come up heads. What is the probability that you picked
the two-headed coin?
"""

import string

vowels = 'AEIOUYaeiouy'
consonants = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

number_of_vowels = 0
number_of_consonants = 0
number_of_punctuation = 0
number_of_spaces = 0
total_characters = 0

for char in text:

    total_characters += 1
    if char in string.vowels:
        number_of_vowels += 1
    elif char in string.punctuation:
        number_of_punctuation += 1
    elif char in string.whitespace:
        number_of_spaces += 1
    elif char in consonants:
        number_of_consonants += 1

print(f'Number of vowels: {number_of_vowels}')
print(f'Number of consonants: {number_of_consonants}')
print(f'Number of punctuation: {number_of_punctuation}')
print(f'Number of spaces: {number_of_spaces}')
print(f'Total characters: {total_characters}')
```


## Random vals

```python
from random import randint

# import random
# random.randint

random_vals = []

for i in range(100):
    random_vals.append(randint(-100, 100))

print(random_vals)
print(sum(random_vals))

negatives = []
positives = []

# for loop

for val in random_vals:

    if val > 0:
        positives.append(val)
    elif val < 0:
        negatives.append(val)
    else: 
        print('zero not included')

print(negatives)
print(positives)

# filter 

negs = list(filter(lambda e: e < 0, random_vals))
posi = list(filter(lambda e: e > 0, random_vals))

print(sum(negs))
print(sum(posi))
```


## Sum 

```python
# calculate sum, min, max
data = '1,2,3,4,5,6,7,8,9,10'
parts = data.split(',')

numbers = []

# riesenie pomocou for
suma = 0
for part in parts:
    num = int(part)
    suma += num
    numbers.append(num)

print(suma)
print(numbers)

# calculate sum, min, max
data = '1,2,3,4,5,6,7,8,9,10'

data2 = list(map(lambda e: int(e), data.split(',')))

print(sum(data2))
print(min(data2))
print(max(data2))
```


## Opakovanie

```python
# calculate sum values with while loop
vals = (1, 2, 3, 4, '5', 6, '7', 8, 9, 10)

# add 3 more users and calculate sum of salaries wit while loop
users = [{'id': 1, 'name': 'Alice', 'salary': 4500}, 
         {'id': 2, 'name': 'Bob', 'salary': 5500}, 
         {'id': 3, 'name': 'Charlie', 'salary': 3000},
         {'id': 4, 'name': 'Tom', 'salary': 2050]

# calcuate sum of even numbers in vals with filter
vals = (23,42,32, 56, 72, 91, 12, 15, 28, 49)

# convert to celsius with map
# formulas: C = (F - 32) * 5/9
fahrenheits = (32, 68, 100, 212, 451)

# calculate character frequency in text with dictionary
text = 'there are seven falcons in the sky and they are flying high'

# generate users with faker, id, first name, last name, email, salary into users.csv file

# read the csv file with csv module and display the data in a table format with prettytable
```


## Riesenia

```python
# calculate sum values with while loop

suma = 0
vals = (1, 2, 3, 4, '5', 6, '7', 8, 9, 10)

i = 0
n = len(vals)

while i < n:
    if type(vals[i]) == str:
        suma += int(vals[i]) 
    else:
        suma += vals[i]

    i += 1

print(suma)
print(sum(map(lambda e: int(e), vals)))


# add 3 more users and calculate sum of salaries with while loop

users = [{'id': 1, 'name': 'Alice', 'salary': 4500}, 
         {'id': 2, 'name': 'Bob', 'salary': 5500}, 
         {'id': 3, 'name': 'Charlie', 'salary': 3000},
         {'id': 4, 'name': 'Tom', 'salary': 2050}]

users.append({'id': 5, 'name': 'Lucia', 'salary': 1230})
users.append({'id': 6, 'name': 'Martin', 'salary': 2330})
users.append({'id': 7, 'name': 'Marcel', 'salary': 1390})

i = 0
n = len(users)
salaries_sum = 0 

while i < n:
    user = users[i]
    salary = user['salary']
    salaries_sum += salary

    i += 1

print(f'The sum of salaries is: {salaries_sum}')


# calcuate sum of even numbers in vals with filter
vals = (23,42,32, 56, 72, 91, 12, 15, 28, 49)
print(sum(filter(lambda e: e % 2 == 0, vals)))

# convert to celsius with map
# formulas: C = (F - 32) * 5/9
fahrenheits = (32, 68, 100, 212, 451)

celsius = list(map(lambda f: round((f - 32) * 5/9, 3), fahrenheits))
print(celsius)

# -------------------------------------------

# calculate letter frequency in text with dictionary
text = 'there are seven falcons in the sky and they are flying high'

freq = {}

for letter in text: 
    if letter == ' ':
        continue
    if letter not in freq:
        freq[letter] = 1
    else:
        freq[letter] += 1

print(freq)

# -------------------------------------------

import faker 

fake = faker.Faker()

filename = 'users.csv' 

with open(filename, 'w') as file:

    file.write("id,first_name,last_name,email,salary\n")
    for i in range(1, 1001):
        uid = i
        first_name  = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        salary = fake.random_int(min=30000, max=100000)
        file.write(f"{uid},{first_name},{last_name},{email},{salary}\n")

# -------------------------------------------

import pandas as pd

df = pd.read_csv('users.csv')

print(df.head())
print(df.tail())
```



## Generate fake data

```python

from faker import Faker

fake = Faker()

filename = 'users.csv'

with open(filename, 'w') as file:
    file.write("uid,first_name,last_name,email,city,country\n")  # Write CSV header
    for i in range(1, 100_001):
        uid = i
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        city = fake.city()
        country = fake.country()

        csv_line = f"{uid},{first_name},{last_name},{email},{city},{country}\n"
        file.write(csv_line)


print(f"Generated {filename} with 100,000 user records.")
```


## Check word count

```python
import sys


# main.py filename firstletter

filename = sys.argv[1]
firstletter = sys.argv[2]

matched_words = []

try:
    with open(filename, 'r') as fd:

        for word in fd:

            if word.lower().startswith(firstletter.lower()):
                matched_words.append(word.strip())
except FileNotFoundError:
    print(f'file {filename} not found')

except Exception as e:
    print(f'an error occurred: {e}')


print(f'there are {len(matched_words)} words starting with {firstletter}')

print('the first 10 words are:')
print(matched_words[0:10])
```

## Check word frequency

```python
import sys


# main.py filename

filename = sys.argv[1]

freq_words = {}

try:
    with open(filename, 'r') as fd:

        for word in fd:
            
            firstletter = word[0]
            if firstletter in freq_words:
                freq_words[firstletter] += 1
            else:
                freq_words[firstletter] = 1

except FileNotFoundError:
    print(f'file {filename} not found')

except Exception as e:
    print(f'an error occurred: {e}')


for key, value in freq_words.items():
    print(f'{key}: {value}')
```


## filter/map

```python


# map/filter

def is_positive(e):

    return e > 0

def is_negative(e):
    
    return e < 0


vals = [3, 4, -2, -1, 5, 33, 0, -5]

positives = list(filter(is_positive, vals))
positives = list(filter(lambda e: e > 0, vals))
print(positives)

negatives = tuple(filter(is_negative, vals))
negatives = tuple(filter(lambda e: e < 0, vals))
print(negatives)


def is_even(e):
    
    return e % 2 == 0


vals = [3, 4, -2, -1, 5, 33, 0, -5]

# custom def function
evens = list(filter(is_even, vals))
print(evens)

# lambda
odds = list(filter(lambda e: e % 2 != 0, vals))
print(odds)


words = ["bad", "cloud", "dog", "war", "water", "cup", "ocean", "small"]

# words_c_w = list(filter(lambda word: word[0] == "c" or word[0] == "w", words))
words_c_w = list(filter(lambda word: word.startswith(("c", "w")), words))
print(words_c_w)


# def twice(e):

#     return e * 2

vals = [4, -3, 0, 1, -4, 0, 9, 3, 2, -3, 6]

vals_doubled = list(map(lambda e: 2*e, vals))
print(vals_doubled)
print(vals)


words = ['cup', "Water", "MOON", 'ALpha', 'smaLL']
words_small = list(map(lambda e: e.lower(), words))
print(words_small)
```


## Passwords

```python
"""
password_checker.py

Checks whether a user-supplied password meets strong-password criteria
and can generate a cryptographically strong password on request.
"""

import secrets
import string
import re


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MIN_LENGTH = 12

SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?"

RULES = [
    ("At least 12 characters",          lambda p: len(p) >= MIN_LENGTH),
    ("At least one uppercase letter",   lambda p: bool(re.search(r"[A-Z]", p))),
    ("At least one lowercase letter",   lambda p: bool(re.search(r"[a-z]", p))),
    ("At least one digit",              lambda p: bool(re.search(r"\d", p))),
    ("At least one special character",  lambda p: any(c in SPECIAL_CHARS for c in p)),
]


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def check_password(password: str) -> tuple[bool, list[str]]:
    """
    Evaluate *password* against every rule in RULES.

    Returns
    -------
    passed : bool
        True when every rule is satisfied.
    failures : list[str]
        Human-readable descriptions of every rule that was NOT met.
    """
    failures = [desc for desc, test in RULES if not test(password)]
    return (len(failures) == 0), failures


def generate_password(length: int = 16) -> str:
    """
    Return a cryptographically strong random password that satisfies all
    rules.  Uses :func:`secrets.choice` so each character is drawn from
    the OS CSPRNG (e.g. /dev/urandom on Linux/macOS).

    The function guarantees at least one character from every required
    category, then fills the remainder with characters drawn from the full
    alphabet and finally shuffles the result so the mandatory characters
    are not always at predictable positions.
    """
    if length < MIN_LENGTH:
        length = MIN_LENGTH

    alphabet = string.ascii_letters + string.digits + SPECIAL_CHARS

    while True:
        # Seed with one character from each mandatory category …
        chars = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice(SPECIAL_CHARS),
        ]
        # … then fill the rest from the full alphabet …
        chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]

        # … shuffle so the mandatory chars are not always at index 0-3 …
        secrets.SystemRandom().shuffle(chars)

        password = "".join(chars)

        # Final sanity-check (should always pass, but belt-and-braces).
        passed, _ = check_password(password)
        if passed:
            return password


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

RESET  = "\033[0m"
GREEN  = "\033[32m"
RED    = "\033[31m"
YELLOW = "\033[33m"
BOLD   = "\033[1m"


def print_result(password: str) -> bool:
    passed, failures = check_password(password)

    print()
    print(f"{BOLD}Password analysis{RESET}")
    print("-" * 40)

    for desc, test in RULES:
        ok = test(password)
        mark = f"{GREEN}✔{RESET}" if ok else f"{RED}✗{RESET}"
        print(f"  {mark}  {desc}")

    print("-" * 40)
    if passed:
        print(f"{GREEN}{BOLD}✔ Strong password — all rules satisfied.{RESET}")
    else:
        print(f"{RED}{BOLD}✗ Weak password — {len(failures)} rule(s) not met.{RESET}")
    print()
    return passed


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"\n{BOLD}=== Password Strength Checker ==={RESET}")
    print("Rules:", ", ".join(f"({i+1}) {d}" for i, (d, _) in enumerate(RULES)))
    print()

    while True:
        print("Options:")
        print("  [1] Test a password")
        print("  [2] Generate a strong password")
        print("  [3] Quit")
        choice = input("\nChoice: ").strip()

        if choice == "1":
            import getpass
            pwd = getpass.getpass("Enter password to test (input hidden): ")
            if not pwd:
                print(f"{YELLOW}No password entered.{RESET}\n")
                continue
            passed = print_result(pwd)
            if not passed:
                suggest = input("Generate a strong password instead? [y/N]: ").strip().lower()
                if suggest == "y":
                    new_pwd = generate_password()
                    print(f"\n{GREEN}Generated password:{RESET} {BOLD}{new_pwd}{RESET}\n")

        elif choice == "2":
            try:
                raw = input("Desired length (default 16): ").strip()
                length = int(raw) if raw else 16
            except ValueError:
                print(f"{YELLOW}Invalid length; using 16.{RESET}")
                length = 16
            pwd = generate_password(length)
            print(f"\n{GREEN}Generated password:{RESET} {BOLD}{pwd}{RESET}")
            print_result(pwd)

        elif choice == "3":
            print("Bye!")
            break

        else:
            print(f"{YELLOW}Please enter 1, 2, or 3.{RESET}\n")


if __name__ == "__main__":
    main()
```


##

```
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
```

```python
try:
    f = 3

    for _ in range(100):
        f = f ** 2
        print(f)

except OverflowError as err:
    print('Overflowed after', f, err)
```

## Opakovanie 

`thermopylae.txt`

```
The Battle of Thermopylae was fought between an alliance of Greek city-states,
led by King Leonidas of Sparta, and the Persian Empire of Xerxes I over the
course of three days, during the second Persian invasion of Greece.
```

```python

# negatives & positives, calculate number, sum, min, max
# no for loops, only while loops
data = """
-1,0,4,-4,4,-1,0,4,-4,5,
-1,0,4,-7,5,-9,-1,0,4,-4,
-1,0,4,-5,3,-1,0,4,-4,5,
-1,0,4,-2,5,5,0,4,9,5
"""

negatives = []
positives = []

data2 = data.replace("\n", "")

parts = data2.split(",")

i = 0
n = len(parts)

while i < n:

    current_element = int(parts[i])

    if current_element > 0:
        positives.append(current_element)
    if current_element < 0:
        negatives.append(current_element)

    i += 1

print(positives, negatives)

print(len(positives))
print(min(positives))
print(max(positives))

print(len(negatives))
print(min(negatives))
print(max(negatives))
```

```python
# negatives & positives, calculate number, sum, min, max
# no for loops, only while loops
data = """
-1,0,4,-4,4,-1,0,4,-4,5,
-1,0,4,-7,5,-9,-1,0,4,-4,
-1,0,4,-5,3,-1,0,4,-4,5,
-1,0,4,-2,5,5,0,4,9,5
"""


# calculate the sum of negative values
vals = (1, 2, 3, 4, 5, -8, -9, -10, 4, 3, 
        -2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8)


# calculate the sum of uniq values
vals2 = (1, 1, 1, 2, 2, 1, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10)

# create a tuple of words that have length 3
words = ['sky', 'bye', 'hello', 'world', 'python', 'programming', 'blue', 
         'to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']

# read the file and count the number of words in the file
file_name = 'thermopylae.txt'
```

## Riesenia

```python
# calculate the sum of negative values

negatives = []
vals = (1, 2, 3, 4, 5, -8, -9, -10, 4, 3, 
        -2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8)

for val in vals:
    if val < 0:
        negatives.append(val)

print(negatives)
print(sum(negatives))
print(sum(e for e in vals if e < 0))

# -----------------------------------

# calculate the sum of uniq values
uniques = []
vals2 = (1, 1, 1, 2, 2, 1, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10)

for val in vals2:
    if val in uniques:
        continue
    else:
        uniques.append(val)

print(sum(uniques))

uniques = set(vals2)
print(sum(uniques))

# -----------------------------------

words = ['sky', 'bye', 'hello', 'world', 'python', 'programming', 'blue', 
         'to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']

words_3 = []

for word in words:
    if len(word) == 3:
        words_3.append(word)

print(words_3)
words_3_t = tuple(words_3)
print(words_3_t)


# ------------------------------------

# read the file and count the number of words in the file
file_name = 'thermopylae.txt'

words = []
with open(file_name, 'r') as fd:

    for line in fd:
        row_words = line.strip().split(' ')
        words.extend(row_words)

print(words)
words_cleaned = []

for word in words:
    if word.count('.') > 0:
        word = word.replace('.', '')
    if word.count(',') > 0:
        word = word.replace(',', '')
    words_cleaned.append(word)

print(words_cleaned)
```


## Task slices


```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

first_three = ...
last_two = ...
every_second = ...

assert (first_three, last_two, every_second) == (['a', 'b', 'c'], ['f', 'g'], ['a', 'c', 'e', 'g'])
print('passed')
```


```python
data = '1,2,3,4,5'

mysum = sum(int(val) for val in data.split(','))

assert mysum == 15
print('passed')
```



data.csv

```
1,2,3,4,5,6,7,8,9,10
11,12,13,14,15,16,17,18,19,20
21,22,23,24,25,26,27,28,29,30
31,32,33,34,35,36,37,38,39,40
41,42,43,44,45,46,47,48,49,50
```

Using csv module 

## calculate sum

```python
import csv

file_name = 'data.csv'

# read -> string
# readlines -> list of rows
# for -> line by line

cleaned_data = []

with open(file_name, mode='r') as file:

    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        for e in row:
            cleaned_data.append(int(e.strip()))

print(sum(cleaned_data))
```

Manual operation

```python

file_name = 'data.csv'

cleaned_values = []


# read -> string
# readlines -> list of rows
# for -> line by line

with open(file_name, mode='r') as file:

    for line in file:
        line_cleaned = line.strip()

        vals = line_cleaned.split(',')
        # print(vals)

        for val in vals:
            cleaned_values.append(int(val))


print(sum(cleaned_values))
```


## open function

```python
file_name = 'words.txt'

cleaned_words = []

with open(file_name, mode='r+') as file:
    
    lines = file.readlines()
    print(lines)

    for line in lines:
        cleaned_line = line.strip()
        cleaned_words.append(cleaned_line)

print(cleaned_words)
```

```python
file_name = 'words.txt'

cleaned_words = []

with open(file_name, mode='r+') as  file:

    for line in file:
        cleaned_words.append(line.rstrip())

print(cleaned_words)
```

## Functions

```python
def g():
    def f():
        print ("f() inner function")
    f()

g()

print(type(g))
print(g.__name__)
print(g.__doc__)
```


## While loop

```python

# print all vowels from the text using while loop
# y is a vowel
msg = 'there are three falcons in the sky'

vowels = 'AEIOUYaeiouy'
# vowels = ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y')

string_len = len(msg)
i = 0 

unique_vowels = set()

while i < string_len:
    if msg[i] in vowels:
        print(msg[i], end=' ')
        unique_vowels.add(msg[i])

    i += 1

print()
print(unique_vowels)
```

## Opakovanie

```python
# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

# calculate sum
data = "1,2,3;4,5;6;7,8,9,10"

# print words starting with 's'
# print words with length == 4
words = ['apple', 'banana', 'small', 'cherry', 'date', 'elderberry', 'war', 
         'peace', 'love', 'happiness', 'sadness', 'joy', 'anger', 
         'fear', 'surprise', 'disgust', 'sorrow', 'sad','happy']

# prints words starting with a in case insensitive way
words = ['Apple', 'ALPINE', 'small', 'car', 'dog', 'cat', 
         'soup', 'salad', 'atom', 'soda', 'art']

# print users older than 30
users = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 30},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25},
    {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28},
    {'first_name': 'Bob', 'last_name': 'Brown', 'age': 35},
    {'first_name': 'Charlie', 'last_name': 'Davis', 'age': 42},
]

users = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 30},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25},
    {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28},
    {'first_name': 'Bob', 'last_name': 'Brown', 'age': 35},
    {'first_name': 'Charlie', 'last_name': 'Davis', 'age': 42},
]

for user in users:
    if user['age'] > 30:
        print(user)

    if user.get('age') > 30:
        print(user)
```

Riesenia

```python
# calculate sum
data = "1,2,3,4,5,6,7,8,9,10"

suma = 0
vals = data.split(",")

for val in vals:
    suma += int(val)

print(suma)


calculate sum

suma = 0

data = "1,2,3;4,5;6;7,8,9,10"
data2 = data.replace(';', ',')

vals = data2.split(',')
for val in vals:
    suma += int(val)


print(suma)

# print words starting with 's'
# print words with length == 4
words = ['apple', 'banana', 'small', 'cherry', 'date', 'elderberry', 'war', 
         'peace', 'love', 'happiness', 'sadness', 'joy', 'anger', 
         'fear', 'surprise', 'disgust', 'sorrow', 'sad','happy']

for word in words:
    if word.startswith('s'):
        print(word)

print('-------------------')

for word in words:
    if len(word) == 4:
        print(word)

# prints words starting with a in case insensitive way
words = ['Apple', 'ALPINE', 'small', 'car', 'dog', 'cat', 
         'soup', 'salad', 'atom', 'soda', 'art']

for word in words:
    if word[0] == 'a' or word[0] == 'A':
        print(word)
```


## Ollama

```
ollama pull granite4.1:3b
```

## startswith/endswith

```python
words = ['war', 'water', 'cup', 'boy', 'cloud', 'warm']

for word in words:
    if word.startswith('w'):
        print(word)

# print('war'.startswith('w'))
# print('war'.endswith('c'))

for word in words:
    if word.endswith('r'):
        print(word)
```

## Slovniky

```python

#!/usr/bin/python

# looping.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway" }

for key in domains:
    print(key, domains[key])

print('--------------------------')

for val in domains.values():
    print(val)

print('--------------------------')


for k, v in domains.items():
    print(k, v)
```



## Opakovanie

```python

# calculate sum of values, using for loop
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# calculate sum of values
data2 = [1, 2, 3, '4', 5, '6', 7, 8, '9', 10]

# calculate sum 

data3 = (
    (1, 2, 3), 
    (4, 5, 6), 
    (7, 8, 9), 
    (10, 11, 12), 
    (13, 14, 5),
    (15, 16, 17), 
    (18, 19, 20), 
    (21, 22, 23), 
    (24, 25, 26), 
    (27, 28, 29), 
    (30, 31, 32), 
    (33, 34, 35), 
    (36, 37, 38), 
    (39, 40, 41), 
    (42, 43, 44), 
    (45, 46, 47), 
    (48, 49, 50), 
    (51, 52, 53), 
    (54, 55, 56), 
    (57, 58, 59)
    )

# create a list of negative an positive numbers from 
# the list
data4 = (3, -2, -5, 7, -1, 0, 6, 3, -4, 2)

# print messages in form John is 25 years old
people = [("John", 25), ("Jane", 30), ("Doe", 22)]

# create a list of 100 random integers between 1 and 100
# verify with len, calculate min, max, and average

```

## Riesenia

```python

# calculate sum of values, using for loop
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(data))

suma = 0 

for num in data:
    suma += num

print(suma)

# calculate sum of values
data2 = [1, 2, 3, '4', 5, '6', 7, 8, '9', 10]

suma = 0
for num in data2:
    if type(num) == str:
        suma += int(num)
    else:
        suma += num

print(suma)

# calculate sum 
data3 = (
    (1, 2, 3), 
    (4, 5, 6), 
    (7, 8, 9), 
    (10, 11, 12), 
    (13, 14, 5),
    (15, 16, 17), 
    (18, 19, 20), 
    (21, 22, 23), 
    (24, 25, 26), 
    (27, 28, 29), 
    (30, 31, 32), 
    (33, 34, 35), 
    (36, 37, 38), 
    (39, 40, 41), 
    (42, 43, 44), 
    (45, 46, 47), 
    (48, 49, 50), 
    (51, 52, 53), 
    (54, 55, 56), 
    (57, 58, 59)
    )

suma = 0

for nested in data3:
    for e in nested:
        suma += e
    # suma += sum(nested)
    # print(nested)

print(suma)
print(len(data3))


data4 = (3, -2, -5, 7, -1, 0, 6, 3, -4, 2)

positive = []
negative = []

for e in data4:
    if e < 0:
        negative.append(e)
    elif e > 0:
        positive.append(e)

print(positive)
print(negative)

# print messages in form John is 25 years old
people = [("John", 25), ("Jane", 30), ("Doe", 22)]

for e in people:
    msg = f'{e[0]} is {e[1]} years old'
    print(msg)

print('-----------------------------')

for name, age in people:
    msg = f'{name} is {age} years old'
    print(msg)

import random

# create a list of 100 random integers between 1 and 100
# verify with len, calculate min, max, and average
random_numbers = []

for _ in range(100):
    r = random.randint(1, 100)
    random_numbers.append(r)


print(len(random_numbers))    
print(min(random_numbers))
print(max(random_numbers))
print(sum(random_numbers)/len(random_numbers))
```


## modifying lists

```python
actors = ["Jack Nicholson", "Antony Hopkins", "Adrien Brody"]

print(actors)

actors.remove("Jack Nicholson")
print(actors)

actors.append('Paul Johnson')
print(actors)
```


## uloha

vypis 11

```python
mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))
```


vypis blue a big

```python
words = ("sun", "moon", ("cat", "dog", ("red", "blue", ("fast", "slow", "big"))))
```


## Rich table

```python
from rich.console import Console
from rich.table import Table

# 1. Initialize the Console object
console = Console()

# 2. Define a dictionary of users
# Using IDs as keys and user details as values
users_data = {
    "USR001": {"name": "Alice Vance", "email": "alice@cyber.net", "role": "Lead Engineer"},
    "USR002": {"name": "Bob Burnquist", "email": "bob@skate.org", "role": "Contributor"},
    "USR003": {"name": "Charlie Day", "email": "charlie@paddys.pub", "role": "Maintenance"},
    "USR004": {"name": "Diana Prince", "email": "diana@themyscira.gov", "role": "Security"},
}

# 3. Create a Table instance
table = Table(title="System User Registry", show_header=True, header_style="bold magenta")

# 4. Define the columns
table.add_column("ID", style="dim", width=8)
table.add_column("Name", style="cyan")
table.add_column("Email", style="green")
table.add_column("Role", justify="right")

# 5. Iterate through the dictionary and add rows to the table
for user_id, info in users_data.items():
    table.add_row(
        user_id, 
        info["name"], 
        info["email"], 
        info["role"]
    )

# 6. Render the table to the console
console.print(table)
```


## rounding

```python
#!/usr/bin/python

import math

val = math.sin(1)

print(f'{val:.2f}')
print(f'{val:.5f}')
print(f'{val:.9f}')

print(round(val))
print(round(val, 2))
print(round(val, 3))
print(round(val, 4))
```


## fstrings

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

msg = 'Hello, ' + name + ', you are ' + str(age) + ' years old.'
print(msg)

msg = f'Hello {name}! You are {age} years old.'
print(msg)
```

## adding script

```python

import sys

print(sys.argv)

suma = 0

for arg in sys.argv[1:]:
    suma += int(arg)

print("the sum of script integer arguments is:", suma)
```


## File attributes

`python file_attribures.py words.txt`

```python
#!/usr/bin/env python3
"""
file_attributes.py – Read and display detailed attributes of a file or
directory. Usage: python file_attributes.py <path>
"""

import os
import sys
import stat
import time
import hashlib
import platform
from pathlib import Path


def format_size(size_bytes: int) -> str:
    """Convert bytes to a human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def format_time(ts: float) -> str:
    """Convert a Unix timestamp to a readable local datetime string."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))


def get_permissions(mode: int) -> str:
    """Return a Unix-style permission string, e.g. -rwxr-xr-x."""
    return stat.filemode(mode)


def get_checksum(path: Path, algorithm: str = "sha256") -> str:
    """Compute a checksum of the file content."""
    h = hashlib.new(algorithm)
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except (OSError, PermissionError) as e:
        return f"<unavailable: {e}>"


def read_attributes(path_str: str) -> None:
    path = Path(path_str).resolve()

    if not path.exists():
        print(f"Error: '{path}' does not exist.")
        sys.exit(1)

    s = path.stat()
    mode = s.st_mode

    print("=" * 60)
    print(f"  FILE ATTRIBUTES: {path.name}")
    print("=" * 60)

    # --- Basic info ---
    print("\n[General]")
    print(f"  Full path    : {path}")
    print(f"  Name         : {path.name}")
    print(f"  Stem         : {path.stem}")
    print(f"  Suffix/Ext   : {path.suffix or '(none)'}")
    print(f"  Parent dir   : {path.parent}")

    # --- Type ---
    print("\n[Type]")
    if path.is_symlink():
        print(f"  Type         : Symbolic link → {os.readlink(path)}")
    elif path.is_dir():
        print("  Type         : Directory")
    elif path.is_file():
        print("  Type         : Regular file")
    else:
        print("  Type         : Special / other")

    # --- Size ---
    print("\n[Size]")
    if path.is_file():
        print(f"  Size         : {format_size(s.st_size)}  ({s.st_size:,} bytes)")
    else:
        print("  Size         : N/A (not a regular file)")

    # --- Timestamps ---
    print("\n[Timestamps]")
    print(f"  Modified     : {format_time(s.st_mtime)}")
    print(f"  Accessed     : {format_time(s.st_atime)}")
    print(f"  Metadata chg : {format_time(s.st_ctime)}")

    # macOS has birth time via st_birthtime
    if hasattr(s, "st_birthtime"):
        print(f"  Created      : {format_time(s.st_birthtime)}")

    # --- Permissions ---
    print("\n[Permissions]")
    print(f"  Mode (octal) : {oct(stat.S_IMODE(mode))}")
    print(f"  Mode (string): {get_permissions(mode)}")
    print(f"  Readable     : {os.access(path, os.R_OK)}")
    print(f"  Writable     : {os.access(path, os.W_OK)}")
    print(f"  Executable   : {os.access(path, os.X_OK)}")

    # --- Ownership (Unix only) ---
    if platform.system() != "Windows":
        import pwd, grp
        try:
            owner = pwd.getpwuid(s.st_uid).pw_name
        except KeyError:
            owner = str(s.st_uid)
        try:
            group = grp.getgrgid(s.st_gid).gr_name
        except KeyError:
            group = str(s.st_gid)
        print(f"  Owner        : {owner} (uid={s.st_uid})")
        print(f"  Group        : {group} (gid={s.st_gid})")

    # --- Filesystem info ---
    print("\n[Filesystem]")
    print(f"  Inode        : {s.st_ino}")
    print(f"  Device       : {s.st_dev}")
    print(f"  Hard links   : {s.st_nlink}")

    # --- Checksum (files only) ---
    if path.is_file():
        print("\n[Checksum]")
        print(f"  MD5          : {get_checksum(path, 'md5')}")
        print(f"  SHA-256      : {get_checksum(path, 'sha256')}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default to the script itself if no argument is given
        target = __file__
        print(f"No path provided. Using script itself as demo: {target}\n")
    else:
        target = sys.argv[1]

    read_attributes(target)
```


mix = (1, 2, 3, (4, 5, 6, (7, 8, 9, (10, 11, 12))))

## Lambdas

```python
nums = [1, 2, 3, 4, 5, 6]

print(min(nums))
print(max(nums))


# def get_price(c):
#     return c.price    

from dataclasses import dataclass

@dataclass(frozen=True)
class Car:
    name: str
    price: int
    production_year: int

cars = [
    Car("Audi", 52642, 2018), Car("Mercedes", 57127, 2019), Car("Skoda", 9000, 2015),
    Car("Volvo", 29000, 2017), Car("Bentley", 350000, 2020), Car("Citroen", 21000, 2016),
    Car("Hummer", 41400, 2014), Car("Volkswagen", 21601, 2013)
]

n = min(cars, key=lambda c: c.production_year)
print(n)

n = max(cars, key=lambda c: c.production_year)
print(n)
```

sorting

```python
#!/usr/bin/python

# cut name into first_name and last_name
users = [
  {'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': 1987},
  {'first_name': 'Jane', 'last_name': 'Doe', 'date_of_birth': 1996},
  {'first_name': 'Robert', 'last_name': 'Brown', 'date_of_birth': 1977},
  {'first_name': 'Lucia', 'last_name': 'Smith', 'date_of_birth': 2002},
  {'first_name': 'Patrick', 'last_name': 'Dempsey', 'date_of_birth': 1994}
]

users.sort(reverse=False, key=lambda user: user['last_name'])

for user in users:
    print(user)
```

## Sum of CSV data


```python
data = '1,2,3,4,5,6,7,8,9,10'

# parts = data.split(',')
# print(parts)

# nums = [int(part) for part in parts]

# print(sum(nums))

print(sum(int(e) for e in data.split(',')))
```



## Fetch web page


```python
import requests

def fetch_homepage():
    """
    Fetches the homepage of https://something.com
    """
    url = "https://something.com"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print("\nPage Content:")
        print(response.text)
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
        return None

if __name__ == "__main__":
    fetch_homepage()
```


## Bar chart

```python
import matplotlib.pyplot as plt

# Simple dataset
categories = ['Apple', 'Banana', 'Cherry', 'Date']
values = [10, 15, 7, 12]

# Create bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Quantities')

# Save the chart as PNG
plt.savefig('bar_chart.png')

print("Bar chart saved as bar_chart.png")
```


## OPenRouter test file

```python
from openai import OpenAI
import os


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# First API call with reasoning
response = client.chat.completions.create(
  model="x-ai/grok-4.1-fast:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="x-ai/grok-4.1-fast:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)

print("Final response:", response2.choices[0].message.content)
```

## Calculate total sales

```python
import re

text = """
Name      | price  | stock |
Product A |      3 | 2312  |
Product B |     12 | 120   |
Procuct C |     21 | 3450  |
Product D |     11 | 12300 |
"""


pattern = re.compile(r'\d+')

found = re.findall(pattern, text)
print(found)
```

```python
import funcy
import re

text = """
Name      | price  | stock |
Product A |      3 | 2312  |
Product B |     12 | 120   |
Procuct C |     21 | 3450  |
Product D |     11 | 12300 |
"""


pattern = re.compile(r'\d+')

found = re.findall(pattern, text)

vals = [int(val) for val in found]
print(vals)

# Using funcy to pair values
pairs = list(funcy.partition(2, vals))

total = 0
for price, stock in pairs:
    total += price * stock
print(f'Total value of products: {total}')

# n = len(vals) // 2
# products = [vals[i:i + 2] for i in range(0, len(vals), 2)]

# prices = [product[0] for product in products]
# print(prices)
# stocks = [product[1] for product in products]
# print(stocks)

# products = [{'price': price, 'stock': stock} for price, stock in zip(prices, stocks)]
# for i, product in enumerate(products):
#     product['name'] = f'Product {chr(65 + i)}'

# print(products)
```


## Calculate sum

```python
import re

text = """
Product A -> 2312 |
Product B -> 120 |
Procuct C -> 3450 |
Product D -> 12300 |
"""

pattern = re.compile(r'[0-9]+')

found = re.findall(pattern, text)

if found:
    print(f'There are {len(found)} numbers')
    print(found)
```



## Opakovanie

```python
# generate a list of 1000 users with id, first_name, last_name, salary 
# with faker

# read into users of dictionaries list
# extract salaries into salaries list 
# calculate min/max/sum/len/mean/median

# using AI model transform the CSV into SQLite SQL and 
# create a database table

# using Python, read the users from the table into a list 
# and print first 20 and last 20 users.
```




## Opakovanie

`users.csv`

```
Roger,Roe,gardener
Peter,Smith,plumber
Paul,Johnson,teacher
Mary,Johnson,teacher
Carol,Smith,doctor
John,Doe,engineer
Richard,Smith,doctor
Susan,Johnson,teacher
Alex,Johnson,engineer
Roman,Walker,programmer
Alice,Wen,artist
```


```python

# generate a list of 500 random salaries from 850 - 1550 with step 50
# calculate sum, min, max, mean, avg of the salaries

# transform to lowercase using list comprehension
words = ["skY", "NEW", "Output", "blue", "SMart", 'oceaN']

# filter even vals using list comprehension
vals = [3, 4, 2, 1, 9, 11, 10, 8, 7, 6, 3]

# using a list comprehension, generate a list of random values
# between 1 .. 100. 

# calculate sum using list comprehension
data = "1;2;3;4;5;6,7;8;9;10"

# filter out words with length 3 and ending in 't'
words2 = ["sky", "war", "put", "out", "ocean", 'os', 'season', 'arch']


# calculate sum
data = """
1,2,3,4,5
6,7,8,9,10
"""


# read the users.csv file and generate a list of dataclass objects
# filter all teachers from the list


# generate a CSV file with faker, with 1250 rows, with these 
# columns: id, first_name, last_name, email, salary
```




`words.txt`


```
sky
blue
dog
spy
Spy
corridor
prime
PRIME
SNOW
cold
warm
RISK
war
WAR
cup
CUP
```



## Opakovanie

```python
# generate a list of cubes
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter all numbers
data = ['test', 3.0, 5, True, (1, 2), 3.14, None, {'us': 'United States'}, 
        [1, 2, 3], 'hello', 42]

# clean the words, remove leading and trailing spaces, and filter out empty strings
words = [' blue', '\nred', '',  'green', '\t\tyellow', 'purple\n', 
         'sky', 'pawn', 'rock\n', '  ', 'paper', '\t\tscissors']

# using list comprehension, generate a list of random numbers 
# from 1, 100 
# print first 10 and last 10 numbers

# calculate the sum of all numbers in the list
data2 = '1,2,3,4,5,6,7,8,9,10'

# filter users youger than 30 years old
# filter users with last name starting with 'W'
from collections import namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'age', 'email'])

users = [
    User('John', 'Doe', 34, 'john.doe@example.com'),
    User('Jane', 'Smith', 28, 'jane.smith@example.com'),
    User('Alice', 'Johnson', 45, 'alice.johnson@example.com'),
    User('Bob', 'Brown', 50, 'bob.brown@example.com'),
    User('Charlie', 'Davis', 22, 'charlie.davis@example.com'),
    User('Emily', 'Wilson', 30, 'emily.wilson@example.com'),
    User('Frank', 'White', 27, 'frank.white@example.com'),
    User('Grace', 'Hall', 38, 'grace.hall@example.com'),
    User('Henry', 'Lewis', 29, 'henry.lewis@example.com'),
    User('Ivy', 'Young', 40, 'ivy.young@example.com'),
    User('Jack', 'Martin', 33, 'jack.martin@example.com'),
    User('Karen', 'King', 26, 'karen.king@example.com'),
    User('Leo', 'Scott', 35, 'leo.scott@example.com'),
    User('Mia', 'Turner', 24, 'mia.turner@example.com'),
    User('Nathan', 'Adams', 37, 'nathan.adams@example.com'),
    User('Olivia', 'Baker', 31, 'olivia.baker@example.com'),
    User('Paul', 'Carter', 42, 'paul.carter@example.com'),
    User('Quinn', 'Flores', 23, 'quinn.flores@example.com'),
    User('Ryan', 'Hill', 48, 'ryan.hill@example.com'),
    User('Sophia', 'Reed', 29, 'sophia.reed@example.com')
]
```



















## Opakovanie

`words.txt`

```
sky
blue
dog
spy
corridor
prime
snow
cold
warm
risk
war
```


```python
# print message using fstring
first_name = 'Roger'
last_name = 'Roe'
occupation = 'gardener'

# create new tuple with elements doubled
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# compute the sum of these values
data = '1,2,3,4,5,6,7,8,9,10'

# filter words starting with 'w'
words = ['sky', 'word', 'worm', 'car', 'type', 
         'car', 'water', 'world']


# create a list of 100 random values
rvals = []

# read words.txt file and print all that 
# start either with 'w' or 'c'
```

## riesenia

```python
# print message using fstring
first_name = 'Roger'
last_name = 'Roe'
occupation = 'gardener'

print(f'{first_name} {last_name} is a {occupation}.')


# create new tuple with elements doubled
vals = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

vals_doubled = []

for val in vals:
    vals_doubled.append(val * 2)

vals_doubled_tuple = tuple(vals_doubled)
print(vals_doubled_tuple)

vals2 = tuple(map(lambda x: x * 2, vals))
print(vals2)

# compute the sum of these values
data = "1,2,3,4,5,6,7,8,9,10"

vals = []

fields = data.split(",")
print(fields)

for e in fields:
    vals.append(int(e))

print(vals)
print(sum(vals))

# print(sum(map(lambda e: int(e), fields)))
print(sum(map(int, fields)))


# filter words starting with 'w'
words = ["sky", "word", "worm", "car", "type", "car", "water", "world"]

words_w = list(filter(lambda word: word[0] == 'w', words))
print(words_w)

words_w = list(filter(lambda word: word.startswith('w'), words))
print(words_w)


words_w_c = list(filter(lambda word: word[0] == 'w' or word[0] == 'c', words))
print(words_w_c)

words_w_c = list(filter(lambda word: word[0] in ('w', 'c'), words))
print(words_w_c)

words_w_c = list(filter(lambda word: word.startswith(('w', 'c')), words))
print(words_w_c)

import random

# create a list of 100 random values, in ranage 1 - 100
rvals = []

for i in range(100):
    rvals.append(random.randint(1, 100))

print(rvals)

file_name = 'words.txt'

with open(file_name, 'r') as fd:
    
    lines = fd.readlines()
    print(lines)
    print(type(lines))

    for line in lines:
        print(line.strip())


    cleaned_lines = list(map(lambda line: line.strip(), lines))
    print(cleaned_lines)

    words_w_c = list(filter(lambda word: word.startswith(('w', 'c')), cleaned_lines))
    print(words_w_c)
```





## Funcy

```python
import funcy

# Sample list of values
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Split into even and odd numbers
evens, odds = funcy.split(lambda x: x % 2 == 0, vals)

print(list(evens))
print(list(odds))
```




```sql
-- Create the 'people' table
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    occupation TEXT
);

-- Insert data into the table
INSERT INTO people (first_name, last_name, occupation) VALUES 
    ('John', 'Doe', 'gardener'),
    ('Roger', 'Doe', 'driver'),
    ('Adam', 'Novak', 'teacher'),
    ('Paul', 'Novak', 'programmer'),
    ('Roman', 'Meszaros', 'programmer'),
    ('Tomas', 'Bruzik', 'driver'),
    ('Lucia', 'Smith', 'teacher'),
    ('Jane', 'Smith', 'teacher');
```






## Functional programming

```python
# def twice(e):
#     return e * 2


vals = [1, 2, 3, 4, 5]

# vals_2 = list(map(twice, vals))
vals_2 = list(map(lambda e: e * 2, vals))

print(vals)
print(vals_2)

vals_3 = [val * 2 for val in vals]
print(vals_3)
```

```python
words = ['hello', 'one', 'world', 'python', 'rocks', 'sky', 'cupcake']

words_3c = list(filter(lambda e: len(e) == 3, words))
print(words_3c)
words_3c = [word for word in words if len(word) == 3]
print(words_3c)
```

procedural style:

```python
words_3c = []

for word in words:
    if len(word) == 3:
        words_3c.append(word)

print(words_3c)
```




```
id,first_name,last_name,occupation,salary
1,Ashley,Curtis,International aid/development worker,6300
2,Christine,Bowman,Immunologist,4200
3,Juan,Howe,Holiday representative,3700
4,Craig,Jordan,Television floor manager,3200
5,Roy,Allen,Engineering geologist,6700
6,Shelly,Rodriguez,Art gallery manager,1100
7,Latoya,Cameron,Geographical information systems officer,6300
8,Renee,Thompson,"Designer, blown glass/stained glass",6800
9,Steven,Mcmillan,Pathologist,6200
10,Jasmine,Holland,"Teacher, adult education",2200
11,Tracy,Wagner,"Solicitor, Scotland",7800
12,Bonnie,Harvey,Systems developer,2600
13,Michael,Roberts,Hydrogeologist,3400
14,Susan,Vaughn,Data processing manager,3300
15,Jessica,Miller,"Designer, exhibition/display",1200
16,Ryan,Jimenez,Chartered accountant,7300
17,Alex,Martinez,"Nurse, children's",4300
18,John,Simmons,"Scientist, audiological",7200
19,Samuel,Francis,Oncologist,1600
20,Eric,Hicks,Podiatrist,3300
21,Billy,Santos,Medical laboratory scientific officer,2800
22,Grant,Johnson,Occupational therapist,4100
23,Stephen,Jimenez,Adult nurse,900
24,Ashley,Garcia,Materials engineer,7700
25,Emily,Brown,"Scientist, research (maths)",6700
26,Catherine,Lopez,Theatre stage manager,1300
27,Jacob,Weeks,"Lecturer, further education",3400
28,Jaime,Smith,Writer,5500
29,Ryan,Hughes,Print production planner,2700
30,Nicole,Graham,Barista,6000
31,Daniel,Galvan,Personal assistant,7500
32,Sarah,Hayes,Advertising account executive,5700
33,Matthew,Hawkins,"Designer, fashion/clothing",2400
34,Bruce,Stewart,Freight forwarder,4700
35,Michele,English,Secretary/administrator,2200
36,Daniel,Martin,Games developer,3600
37,Ashley,Smith,Theme park manager,7200
38,Chris,Gonzalez,Product manager,6600
39,Kristen,Miller,Marine scientist,6800
40,Cindy,Silva,General practice doctor,4300
41,Melissa,Stone,Research scientist (physical sciences),4200
42,Jean,Wilson,Child psychotherapist,7300
43,Marcus,Carlson,Transport planner,6300
44,Scott,Gordon,"Engineer, automotive",3300
45,Susan,Wells,Lobbyist,2800
46,Victoria,French,Operational researcher,7100
47,Joseph,Henry,Farm manager,6500
48,Patrick,Collins,Nature conservation officer,5200
49,Joann,Ross,Research scientist (maths),7200
50,Bob,Romero,Operational researcher,7800
51,Wayne,Marks,Nature conservation officer,4500
52,Lori,Thompson,Environmental consultant,4200
53,Duane,Barber,Veterinary surgeon,4500
54,Emily,Lutz,Field seismologist,4600
55,Theresa,Cook,Psychiatric nurse,2800
56,Danielle,Ramos,Community education officer,4300
57,Kendra,Vazquez,"Merchandiser, retail",4800
58,Christopher,Gordon,"Engineer, broadcasting (operations)",4200
59,Gabriel,Nguyen,Theme park manager,5900
60,Chad,Thompson,"Solicitor, Scotland",3800
61,Kevin,Ramirez,Aeronautical engineer,6300
62,Chad,Bell,"Surveyor, rural practice",3200
63,Tina,Hull,Licensed conveyancer,5500
64,Kristin,Brown,Primary school teacher,1700
65,Stacy,Peterson,"Therapist, speech and language",4900
66,Cheryl,Wu,Homeopath,1400
67,Ernest,Howard,Agricultural consultant,3700
68,Teresa,Andersen,Architectural technologist,6900
69,Amber,Guzman,Haematologist,5100
70,Michelle,Porter,"Therapist, music",3900
71,Douglas,Wood,"Embryologist, clinical",1000
72,Emily,Salazar,Higher education lecturer,6600
73,Daniel,Roberts,Aeronautical engineer,5700
74,Chad,Powell,Phytotherapist,4500
75,Calvin,Roach,"Editor, commissioning",5200
76,Daniel,Rodriguez,Network engineer,2100
77,David,Bradford,Transport planner,4500
78,Stanley,Weber,Rural practice surveyor,5800
79,Whitney,Macias,Landscape architect,4800
80,Deborah,Berry,Theme park manager,5700
81,Debra,Buchanan,Lawyer,6300
82,Eric,Willis,"Psychologist, forensic",5000
83,Mark,Cox,Ecologist,6700
84,Justin,Jones,Television floor manager,1300
85,Christopher,Flores,Financial trader,3200
86,Sarah,Ward,"Accountant, chartered management",3300
87,Jared,Norris,Press sub,5300
88,Blake,Henry,"Programmer, systems",1200
89,Michael,Watkins,Hydrogeologist,4900
90,Charles,Warren,Purchasing manager,1600
91,Madison,Clark,Museum/gallery conservator,2000
92,Lisa,Mullins,Broadcast journalist,5000
93,Erik,Curry,Broadcast journalist,2500
94,Katherine,Cooper,Immunologist,3600
95,Kelly,Gonzalez,Ship broker,5400
96,Kristin,Friedman,Site engineer,4000
97,Dustin,Huynh,Pension scheme manager,2100
98,Jon,Perez,Insurance account manager,3800
99,Anthony,Duncan,Geographical information systems officer,7500
100,John,Andrews,"Clinical scientist, histocompatibility and immunogenetics",3700
```




```sql
CREATE TABLE users(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, occupation TEXT, salary INT);
```



## SQL INJECTION

```python
import sqlite3

name = 'Bratislava'
population = 432000

con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()    

    # DO NOT DO THIS, IT IS DANGEROUS, SQL INJECTION
    # print(f"UPDATE cities SET population={population} WHERE name='{name}'")
    # cur.execute(f"UPDATE cities SET population={population} WHERE name='{name}'")
    # cur.execute("UPDATE cities SET population=" + str(population) + " WHERE name= " + name)

    # parameterized query
    cur.execute("UPDATE cities SET population=? WHERE name=?", (population, name))           
    print("Number of rows updated: {}".format(cur.rowcount))
```



## Opakovanie

`users_20.csv`

```
id,first_name,last_name,occupation,salary
1,Ashley,Curtis,International aid/development worker,6300
2,Christine,Bowman,Immunologist,4200
3,Juan,Howe,Holiday representative,3700
4,Craig,Jordan,Television floor manager,3200
5,Roy,Allen,Engineering geologist,6700
6,Shelly,Rodriguez,Art gallery manager,1100
7,Latoya,Cameron,Geographical information systems officer,6300
8,Renee,Thompson,"Designer, blown glass/stained glass",6800
9,Steven,Mcmillan,Pathologist,6200
10,Jasmine,Holland,"Teacher, adult education",2200
11,Tracy,Wagner,"Solicitor, Scotland",7800
12,Bonnie,Harvey,Systems developer,2600
13,Michael,Roberts,Hydrogeologist,3400
14,Susan,Vaughn,Data processing manager,3300
15,Jessica,Miller,"Designer, exhibition/display",1200
16,Ryan,Jimenez,Chartered accountant,7300
17,Alex,Martinez,"Nurse, children's",4300
18,John,Simmons,"Scientist, audiological",7200
19,Samuel,Francis,Oncologist,1600
20,Eric,Hicks,Podiatrist,3300
```


```python
# get status code of https://example.com

import requests
url = "https://example.com"
...

# ==========================================================

# get home page of https://something.com 
# and save it to home.html
import requests
url = "https://something.com"
...

# ==========================================================

prices = [1.5, 2.0, 3.75, 4.25]

total_with_tax = ...  # Add 10% tax to sum of prices

assert total_with_tax == 13.75
print('passed')

# ==========================================================

items = {'apple': 2, 'banana': 3, 'orange': 1}

total_items = ...

assert total_items == 6
print('passed')

# ==========================================================

# read users_20.csv and print the first 5 rows the followng way
# Ashley Curtis is International aid/development worker with salary 6300
import csv

file_name = 'users_20.csv'

with open(file_name, 'r') as fd:
    reader = csv.reader(fd)
    ...

# ==========================================================


# print first 5 and last 5 todos from https://jsonplaceholder.typicode.com/todos
import requests

url = "https://jsonplaceholder.typicode.com/todos"
```




## Riesenia

```python
import requests
url = "https://example.com"

resp = requests.get(url)
status_code = resp.status_code
print(status_code)


# get home page of https://something.com 
# and save it to home.html
import requests
url = "https://something.com"

resp = requests.get(url)
file_name = 'home.html'

content = resp.text

with open(file_name, 'w') as fd:
    fd.write(content)

prices = [1.5, 2.0, 3.75, 4.25]


total_with_tax = sum(prices) * 1.1

assert total_with_tax == 12.65
print('passed')



items = {'apple': 2, 'banana': 3, 'orange': 1}

total_items = sum(items.values())

assert total_items == 6
print('passed')



# read users_20.csv and print the first 5 rows the followng way
# Ashley Curtis is International aid/development worker with salary 6300
import csv

file_name = 'users_20.csv'

users = []
with open(file_name, 'r') as fd:
    reader = csv.reader(fd)
    
    next(reader)  # skip header

    for row in reader:
        users.append(row)

for users in users[:5]:

    first_name = users[1]
    last_name = users[2]
    job = users[3]
    salary = users[4]
    print(f"{first_name} {last_name} is {job} with salary {salary}")


# read users_20.csv and print the first 5 rows the followng way
# Ashley Curtis is International aid/development worker with salary 6300
import csv

file_name = 'users_20.csv'

users = []
with open(file_name, 'r') as fd:
    reader = csv.DictReader(fd)
    
    for row in reader:
        users.append(row)

for users in users[:5]:

    first_name = users['first_name']
    last_name = users['last_name']
    job = users['occupation']
    salary = users['salary']
    print(f"{first_name} {last_name} is {job} with salary {salary}")




# print first 5 and last 5 todos from https://jsonplaceholder.typicode.com/todos
import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
todos = response.json()

print("First 5 todos:")
print(todos[:5])

print("\nLast 5 todos:")
print(todos[-5:])


```















## CSV to JSON

```python
import csv
import json

# Define input and output file names
csv_filename = "test_users.csv"
json_filename = "test_users.json"

# Read CSV and convert to JSON
data = []
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert salary from string to integer
        row["salary"] = int(row["salary"])
        data.append(row)

# Write JSON data to file
with open(json_filename, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"CSV data successfully written to {json_filename}")
```




## process CSV data

```python
import csv
import statistics

file_name = 'test_users.csv'

salaries = []

with open(file_name, 'r') as f:

    reader = csv.DictReader(f)
    
    salaries = [int(row['salary']) for row in reader]

    print(f"Total number of salaries: {len(salaries)}")
    print(f"Minimum salary: {min(salaries)}")
    print(f"Maximum salary: {max(salaries)}")
    print(f"Average salary: {sum(salaries) / len(salaries)}")
    print(f"Median salary: {statistics.median(salaries)}")
```


## generate test CSV data

```python
from faker import Faker
import csv

faker = Faker()

with open('test_users.csv', 'w', newline='') as f:

    fieldnames = ['id', 'first_name', 'last_name', 'occupation', 'salary']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(1, 100_000):

        _id = i
        fname = faker.first_name()
        lname = faker.last_name()
        occupation = faker.job()
        salary = faker.random_int(min=800, max=8000, step=100)

        writer.writerow({'id': _id, 'first_name': fname, 
            'last_name': lname, 'occupation': occupation, 'salary': salary})
```




## Transform JSON into CSV

```python
import requests
import csv

url = 'https://webcode.me/users.json'

resp = requests.get(url)

if resp.status_code == 200:
    data = resp.json()

    print(data)

    file_name = 'users.csv'
    headers = ['id', 'first_name', 'last_name', 'email']
    with open(file_name, 'w') as fd:
        writer = csv.DictWriter(fd, fieldnames=headers, lineterminator='\n')

        writer.writeheader()
        for user in data["users"]:
            writer.writerow(user)
```

---

The `users.json` file:

```
{
  "users": [
    {
      "id": 1,
      "first_name": "Robert",
      "last_name": "Schwartz",
      "email": "rob23@gmail.com"
    },
    {
      "id": 2,
      "first_name": "Lucy",
      "last_name": "Ballmer",
      "email": "lucyb56@gmail.com"
    },
    {
      "id": 3,
      "first_name": "Anna",
      "last_name": "Smith",
      "email": "annasmith23@gmail.com"
    },
    {
      "id": 4,
      "first_name": "Robert",
      "last_name": "Brown",
      "email": "bobbrown432@yahoo.com"
    },
    {
      "id": 5,
      "first_name": "Roger",
      "last_name": "Bacon",
      "email": "rogerbacon12@yahoo.com"
    }
  ]
}
```




```python
import csv
import json


def read_json_file(file_name):
    with open(file_name, 'r') as fd:
        data = json.load(fd)
        return data

def write_json_file(file_name, data):

    headers = ['id', 'first_name', 'last_name', 'email']
    with open(file_name, 'w') as fd:
        writer = csv.DictWriter(fd, fieldnames=headers, lineterminator='\n')

        writer.writeheader()
        for user in data["users"]:
            writer.writerow(user)


data = read_json_file('users.json')
write_json_file('users.csv', data)
```


## read users.csv file

```python
import csv
import statistics

file_name = "users.csv"

with open(file_name, 'r') as f:

    reader = csv.DictReader(f)

    salaries = []

    for row in reader:

        # print(row)
        print(row['first_name'], row['last_name'], row['salary'])
        salaries.append(int(row['salary']))


    print(salaries)
    print("Average salary: ", statistics.mean(salaries))
    print("Median salary: ", statistics.median(salaries))
```



`users.csv` file

```csv
id,first_name,last_name,salary
1,John,Doe,50000
2,Jane,Smith,60000
3,Bob,Johnson,55000
4,Alice,Williams,70000
5,Charlie,Brown,45000
```




## CSV read file

```python
import csv

file_name = "data.csv"

with open(file_name, 'r') as f:

    reader = csv.reader(f)

    suma = 0
    for row in reader:

        # print(row)

        for field in row:
            suma += int(field)
            
    print(suma)
```



## Retrieve and write HTML page

```python
import requests 

url = 'https://webcode.me/'
resp = requests.get(url)

# print(resp.content.decode('utf-8'))
content = resp.text

with open('home_page.html', 'w') as fd:
    fd.write(content)
```


## Read JSON from URL

```python
import requests

url = "https://webcode.me/users.json"

response = requests.get(url)
data = response.json()

print(data)


for user in data['users']:
    print(f"Name: {user['id']}, First Name: {user['first_name']}, last Name: {user['last_name']}, Email: {user['email']}")

emails = [user['email'] for user in data['users']]

print(emails)
```


## Reading JSON file

```python
import json

fname = 'products.json'
with open(fname) as f:

    data = json.load(f)
    total_sales = 0

    for product in data['products']:
        print(product)

        total_sales = total_sales + float(product['price']) * int(product['quantity'])

    print(f'Total sales: {total_sales}')
```



















```python
import sys
from faker import Faker

filename = sys.argv[1]
n = int(sys.argv[2])

faker = Faker()

with open(filename, 'w') as fd:

    headers = 'id,first_name,last_name,email,city\n'
    fd.write(headers)

    for uid in range(1, n+1):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        row = f'{uid},{first_name},{last_name},{email},{city}\n'

        fd.write(row)
```


```python

import sys

vals = sys.argv[1:]
print(vals)

total = sum(int(val) for val in vals)
print(total)
```



## Generate fake users.csv file

```python

from faker import Faker

faker = Faker()
filename = "users.csv"

with open(filename, 'w') as fd:

    headers = 'id,first_name,last_name,email,city\n'
    fd.write(headers)

    for uid in range(1, 100_001):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        row = f'{uid},{first_name},{last_name},{email},{city}\n'

        fd.write(row)
```



## Write to file

```python
filename = "words2.txt"

with open(filename, 'w') as fd:

    fd.write('atom\n')
    fd.write('new\n')
    fd.write('small\n')
```


## Append to file

```python

filename = "words2.txt"

with open(filename, 'a') as fd:

    fd.write('cup\n')
    fd.write('cloud\n')
```


## reading files

```python
filename = "words.txt"

with open(filename, 'r') as fd:

    # content = fd.read()
    # print(content.split())

    # lines = fd.readlines()
    # print(lines)

    for line in fd:
        print(line.strip())
```



## dataclasses and namedtuples

```python

from dataclasses import dataclass

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    occupation: str
    salary: int


u = User(1, 'Roger', 'Roe', 'driver', 1780)

print(u.last_name)
print(u.salary)

print(u)


# from collections import namedtuple
#
# User = namedtuple('User', 'id first_name last_name occupation salary')
#
# u1 = User(1, "John", "Doe", "gardener", 2300)
# print(u1)
```






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



