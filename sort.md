# Sorting


In computer science, sorting is arranging elements in an ordered sequence. Over  
the years, several algorithms were developed to perform sorting on data,  
including merge sort, quick sort, selection sort, or bubble sort. (The other  
meaning of sorting is categorizing; it is grouping elements with similar  
properties.)  

The opposite of sorting, rearranging a sequence of elements in a random or  
meaningless order, is called shuffling.  


Data can be sorted alphabetically or numerically. The sort key specifies the  
criteria used to perform the sort. It is possible to sort objects by multiple  
keys. For instance, when sorting users, the names of the users could be used as  
primary sort key, and their occupation as the secondary sort key.  

## Sorting order

A standard order is called the ascending order: a to z, 0 to 9. The reverse  
order is called the descending order: z to a, 9 to 0. For dates and times,  
ascending means that earlier values precede later ones e.g. 1/1/2020 will sort  
ahead of 1/1/2021.  

## Stable sort

A stable sort is one where the initial order of equal elements is preserved.  
Some sorting algorithms are naturally stable, some are unstable. For instance,  
the merge sort and the bubble sort are stable sorting algorithms. On the other  
hand, heap sort and quick sort are examples of unstable sorting algorithms.  

Consider the following values: 3715**5**93. A stable sorting produces the  
following: 1335**5**79. The ordering of the values 3 and 5 is kept. An unstable  
sorting may produce the following: 133**5**579.  

Python uses the timsort algorithm. It is a hybrid stable sorting algorithm,  
derived from merge sort and insertion sort. It was implemented by Tim Peters in  
2002 for use in the Python programming language.  

## Python sort functions

Python has two basic function for sorting lists: `sort` and `sorted`. The `sort`  
sorts the list in place, while the `sorted` returns a new sorted list from the  
items in iterable. Both functions have the same options: `key` and `reverse`.  
The `key` takes a function which will be used on each value in the list being  
`sorted` to determine the resulting order. The `reverse` option can reverse the  
comparison order.

Both functions produce stable sorting.  

## Sort list in-place

The `sort` function of the list container modifies the original list when doing  
the sorting.  

```python
words = ['forest', 'wood', 'tool', 'arc', 'sky', 'poor', 'cloud', 'rock']
vals = [2, 1, 0, 3, 4, 6, 5, 7]

words.sort()
print(words)

vals.sort()
print(vals)
```

In the example, we sort the list of strings and integers. The original lists are  
modified.


## The sorted example

The `sorted` function does not modify the original list; rather, it creates a  
new modified list.

```python
words = ['forest', 'wood', 'brisk', 'tree', 'sky', 'cloud', 'rock', 'falcon']

sorted_words = sorted(words)
print('Original:', words)
print('Sorted:', sorted_words)
```

The example creates a new sorted list of words from the original list, which is  
intact.  


## Sort list in ascending/descending order

The ascending/descending order is controlled with the reverse option.  

```python
words = ['forest', 'wood', 'tool', 'arc', 'sky', 'poor', 'cloud', 'rock']

words.sort()
print(words)

words.sort(reverse=True)
print(words)
```

The example sorts the list of words in ascending and descending order.


## Sort list of dates

In the next example, we sort a list of dates.

```python
from datetime import datetime

values = ['8-Nov-19', '21-Jun-16', '1-Nov-18', '7-Apr-19']
values.sort(key=lambda d: datetime.strptime(d, "%d-%b-%y"))

print(values)
```

The anonymous function uses the `strptime` function, which creates a datetime  
object from the given string. Effectively, the sort function sorts datetime  
objects.  

## Sort list by element index

A Python list can have nested iterables. In such cases, we can choose the  
elements which should be sorted.  

```python
vals = [(4, 0), (0, -2), (3, 5), (1, 1), (-1, 3)]

vals.sort()
print(vals)

vals.sort(key=lambda e: e[1])
print(vals)
```

The example sorts the nested tuples initally by their first elements, then by  
their second.  

```python
vals.sort(key=lambda e: e[1])
```

By providing an anonymous function which returns the second element of the  
tuple, we sort the tuples by their second values.  

## Sort list by sum of nested list

Say we have nested lists which all have some various rankings. The final ranking  
is the sum of all the values.  

```python
data = [[10, 11, 12, 13], [9, 10, 11, 12], [8, 9, 10, 11], [10, 9, 8, 7],
    [6, 7, 8, 9], [5, 5, 5, 1], [5, 5, 5, 5], [3, 4, 5, 6], [10, 1, 1, 2]]

data.sort()
print(data)

data.sort(key=sum)
print(data)
```

By default, the sorting functions sort by the first value of the nested lists.  
To achieve our goal, we pass the built-in `sum` function to the key option.  

## Sort list of localized strings

For locale aware sorting, we can use the `locale.strxfrm` for the `key`  
function.

```python
import locale

#
# a á ä b c č d ď dz dž e é f g h ch i í j k l ĺ ľ m n ň o ó ô p q r ŕ s š t ť u ú v w x y ý z ž
#

#
# а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я
#

ru_words = ['земля', 'черника', 'дерево', 'виноград', 'гора', 'джем', 'элемент',
            'щебет', 'дорога', 'ежевика', 'дятел', 'ром', 'железо', 'источник', 'северный олень',
            'хобот', 'хмель', 'пахта', 'сок', 'клевать']

sk_words = ['zem', 'čučoriedka', 'drevo', 'hrozno', 'hora', 'džem', 'element',
            'štebot', 'cesta', 'černice', 'ďateľ', 'rum', 'železo', 'prameň', 'sob',
            'chobot', 'chmel', 'cmar', 'džús', 'dzekať']

locale.setlocale(locale.LC_COLLATE, ('sk_SK', 'UTF8'))

sk_words.sort(key=locale.strxfrm)

for word in sk_words:
    print(word)

print('-----------------------------')

locale.setlocale(locale.LC_COLLATE, ('ru_RU', 'UTF8'))

ru_words.sort(key=locale.strxfrm)

for word in ru_words:
    print(word)

```

The example sorts Slovak and Russian words.



## Python  sort list of dictionaries 

When sorting dictionaries, we can choose the property by which the sorting is performed.  

```python
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

We have a list of users. Each user is represented by a dictionary.  

```python
users.sort(reverse=True, key=lambda e: e['date_of_birth'])
```

In the anonymous function, we choose the date_of_birth property.

```
$ ./sort_dict.py
{'name': 'Lucia Smith', 'date_of_birth': 2002}
{'name': 'Jane Doe', 'date_of_birth': 1996}
{'name': 'Patrick Dempsey', 'date_of_birth': 1994}
{'name': 'John Doe', 'date_of_birth': 1987}
{'name': 'Robert Brown', 'date_of_birth': 1977}
```

The users are sorted by their date of birth in descending order.

## Sort list of grades

There are various grading systems around the world. Our example contains grades  
such as A+ or C- and these cannot be ordered lexicographically. We use a  
dictionary where each grade has its given value.  

```python
data = 'A+ A A- B+ B B- C+ C C- D+ D'
grades = { grade: idx for idx, grade in enumerate(data.split()) }

def mc(e):
    return grades.get(e[1])

students = [('Anna', 'A+'), ('Jozef', 'B'), ('Rebecca', 'B-'), ('Michael', 'D+'),
    ('Zoltan', 'A-'), ('Jan', 'A'), ('Michelle', 'C-'), ('Sofia', 'C+')]

print(grades)

students.sort(key=mc)
print(students)

# from operator import itemgetter
# students.sort(key=lambda e: itemgetter(e[1])(grades))
```

We have a list of students. Each student has a name and a grade in a nested  
tuple.  

```python
data = 'A+ A A- B+ B B- C+ C C- D+ D'
grades = { grade: idx for idx, grade in enumerate(data.split()) }
```

We build the dictionary of grades. Each grade has its value. The grades will be  
sorted by their dictionary value.  

```python
def mc(e):
    return grades.get(e[1])
```

The `key` function simply returns the value of the grade.

```python
# from operator import itemgetter
# students.sort(key=lambda e: itemgetter(e[1])(grades))
```

This solution uses an anonymous function.

## Sort list by string length

Sometimes, we need to sort the strings by their length.

```python
def w_len(e):
  return len(e)

words = ['forest', 'wood', 'tool', 'sky', 'poor', 'cloud', 'rock', 'if']

words.sort(reverse=True, key=w_len)

print(words)
```

In this example, we do not use an anonymous function.

```python
def w_len(e):
  return len(e)
```

The `w_len` function returns the length of each of the elements.  


## Sort list by case

By default, the strings with uppercase first letters are sorted before the other  
strings. We can sort strings regardless of their case as well.  

```python
text = 'Today is a beautiful day. Andy went fishing.'
words = text.replace('.', '')

sorted_words = sorted(words.split(), key=str.lower)
print('Case insensitive:', sorted_words)

sorted_words2 = sorted(words.split())
print('Case sensitive:', sorted_words2)
```

By providing the `str.lower` function to the `key` attribute, we perform a case  
insensitive sorting.  


## Sort list by lastname

In the following example, we sort the names by last name.

```python
names = ['John Doe', 'Jane Doe', 'Robert Brown', 'Robert Novak',
    'Lucia Smith', 'Patrick Dempsey', 'George Marshall', 'Alan Brooke',
    'Harold Andras', 'Albert Doe']

names.sort()
names.sort(key=lambda e: e.split()[-1])


for name in names:
    print(name)
```

We have a list of names. Each name consists of a first name and last name. In  
addition, there are several users with the same last name. In such a case, we  
want them to be sorted by their first names.  

```python
names.sort()
names.sort(key=lambda e: e.split()[-1])
```

First, we sort the names by their first names. Then we sort the names by their  
last name. To do so, we split each string and choose the last string (it has  
index -1.) Since Python's sort algorithm is stable, the first sorting is  
remembered and we get the expected output.  

```
$ ./sort_by_lastname.py
Harold Andras
Alan Brooke
Robert Brown
Patrick Dempsey
Albert Doe
Jane Doe
John Doe
George Marshall
Robert Novak
Lucia Smith
```

The names are sorted by their last names. The Doe users are correctly sorted by  
their first names.  


## Sort list of dataclasses

In the next example, we sort a list of dataclasses.

```python
from dataclasses import dataclass
from operator import attrgetter

@dataclass
class City:
    id: int
    name: str
    population: int


c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Berlin', 3671000)

cities = [c1, c2, c3, c4, c5, c6, c7]

cities.sort(key=lambda e: e.name)
# cities.sort(key=attrgetter('id'))

for city in cities:
    print(city)
```

We provide the key function as a lambda or use the `attrgetter` function.  

## Sort list of namedtuples

In the next example, we sort namedtuples.

```python
from typing import NamedTuple


class City(NamedTuple):
    id: int
    name: str
    population: int


c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Berlin', 3671000)

cities = [c1, c2, c3, c4, c5, c6, c7]

cities.sort(key=lambda e: e.name)

for city in cities:
    print(city)
```

The `City` namedtuple has three attributes: `id`, `name`, and `population`. The  
example sorts the namedtuples by their names.  

```python
cities.sort(key=lambda e: e.name)
```

The anonymous function returns the `name` property of the namedtuple.


## The itemgetter and attrgetter functions

Python provides the `itemgetter` and `attrgetter` convenience functions to make  
accessor functions easier and faster. They are located in the `operator` module.  

```python
from typing import NamedTuple
from operator import itemgetter, attrgetter

class City(NamedTuple):
    id: int
    name: str
    population: int

c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Berlin', 3671000)

cities = [c1, c2, c3, c4, c5, c6, c7]

sorted_cities = sorted(cities, key=attrgetter('name'))

for city in sorted_cities:
    print(city)

print('---------------------')

sorted_cities = sorted(cities, key=itemgetter(2))

for city in sorted_cities:
    print(city)
```

We sort a list of cities using sorted and the helper functions.

```python
sorted_cities = sorted(cities, key=attrgetter('name'))
```

We pass the attribute name by which we sort the cities.

```python
sorted_cities = sorted(cities, key=itemgetter(2))
```

In case of `itemgetter`, we pass the attribute's index.

## Sort list by multiple sort criteria

The following example sorts a list of students by two sorting criteria.  

```python
from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    grade: str
    age: int

s1 = Student(1, 'Patrick', 'A', 21)
s2 = Student(2, 'Lucia', 'B', 19)
s3 = Student(3, 'Robert', 'C', 19)
s4 = Student(4, 'Monika', 'A', 22)
s5 = Student(5, 'Thomas', 'D', 20)
s6 = Student(6, 'Petra', 'B', 18)
s6 = Student(7, 'Sofia', 'A', 18)
s7 = Student(8, 'Harold', 'E', 22)
s8 = Student(9, 'Arnold', 'B', 23)

students = [s1, s2, s3, s4, s5, s6, s7, s8]
students.sort(key=lambda s: (s.grade, s.age))

for student in students:
    print(student)
```

We sort the students by grades and then by age. The sorting is in asceding order.  

```python
students.sort(key=lambda s: (s.grade, s.age))
```

To do the sorting, we pass the lambda function a tuple of sorting attributes.  

```
$ ./multiple_sort.py
Student(id=7, name='Sofia', grade='A', age=18)
Student(id=1, name='Patrick', grade='A', age=21)
Student(id=4, name='Monika', grade='A', age=22)
Student(id=2, name='Lucia', grade='B', age=19)
Student(id=9, name='Arnold', grade='B', age=23)
Student(id=3, name='Robert', grade='C', age=19)
Student(id=5, name='Thomas', grade='D', age=20)
Student(id=8, name='Harold', grade='E', age=22)
```

We may want to sort the data by multiple criteria with various ordering types.  

The first solution is to wrap the key in a class which defines the ordering  
type.

```python
from typing import NamedTuple

class negate:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


class Student(NamedTuple):
    id: int
    name: str
    grade: str
    age: int


s1 = Student(1, 'Patrick', 'A', 21)
s2 = Student(2, 'Lucia', 'B', 19)
s3 = Student(3, 'Robert', 'C', 19)
s4 = Student(4, 'Monika', 'A', 22)
s5 = Student(5, 'Thomas', 'D', 20)
s6 = Student(6, 'Petra', 'B', 18)
s6 = Student(7, 'Sofia', 'A', 18)
s7 = Student(8, 'Harold', 'E', 22)
s8 = Student(9, 'Arnold', 'B', 23)

students = [s1, s2, s3, s4, s5, s6, s7, s8]
students.sort(key=lambda s: (s.grade, negate(s.age)))

for student in students:
    print(student)
```

The example sorts students by grade in asceding order and then by age in  
descending order.  

```python
students.sort(key=lambda s: (s.grade, negate(s.age)))
```

The second key is wrapped with negate.

```
$ ./multi_sort2.py
Student(id=4, name='Monika', grade='A', age=22)
Student(id=1, name='Patrick', grade='A', age=21)
Student(id=7, name='Sofia', grade='A', age=18)
Student(id=9, name='Arnold', grade='B', age=23)
Student(id=2, name='Lucia', grade='B', age=19)
Student(id=3, name='Robert', grade='C', age=19)
Student(id=5, name='Thomas', grade='D', age=20)
```

Another solution is to sort the list twice.  

```python
from typing import NamedTuple
from operator import attrgetter

def multi_sort(data, specs):

    for key, reverse in reversed(specs):
        data.sort(key=attrgetter(key), reverse=reverse)
    return data


class Student(NamedTuple):
    id: int
    name: str
    grade: str
    age: int


s1 = Student(1, 'Patrick', 'A', 21)
s2 = Student(2, 'Lucia', 'B', 19)
s3 = Student(3, 'Robert', 'C', 19)
s4 = Student(4, 'Monika', 'A', 22)
s5 = Student(5, 'Thomas', 'D', 20)
s6 = Student(6, 'Petra', 'B', 18)
s6 = Student(7, 'Sofia', 'A', 18)
s7 = Student(8, 'Harold', 'E', 22)
s8 = Student(9, 'Arnold', 'B', 23)

students = [s1, s2, s3, s4, s5, s6, s7, s8]

multi_sort(students, (('grade', False), ('age', True)))

for student in students:
    print(student)
```

First, the students are sorted by grades in ascending order, then they are  
sorted by age in descending order.  

```python
def multi_sort(data, specs):

    for key, reverse in reversed(specs):
        data.sort(key=attrgetter(key), reverse=reverse)
    return data
```

The `multi_sort` function applies all the sorting specs on the list.

## Sorting poker cards 

```python
import random
from itertools import groupby


def create_deck():

    signs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    symbols = ['♠', '♥', '♦', '♣']  # spades, hearts, diamonds, clubs

    deck = [f'{si}{sy}' for si in signs for sy in symbols]

    return deck


def by_poker_order(card):

    poker_order = "2 3 4 5 6 7 8 9 10 J Q K A"

    return poker_order.index(card[:-1])


def by_suit(card):

    return card[-1]


deck = create_deck()

print(deck)
random.shuffle(deck)
print(deck)

# Sort by poker order and then by suit
deck.sort(key=by_poker_order)
deck.sort(key=by_suit)

for k, g in groupby(deck, key=lambda c: c[-1]):
    print(k, list(g))
```



