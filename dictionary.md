# Dictionary

A *Python dictionary* is a mutable container of key-value pairs, also called an associative
array or hash table in other languages. Keys must be unique and immutable, such as strings,
numbers, or tuples; values can be of any type. Since Python 3.7, dictionaries preserve
the insertion order of their pairs.

## Creation

First, we show how to create Python dictionaries.

```python

weekend = { "Sun": "Sunday", "Mon": "Monday" }
vals = dict(one=1, two=2)

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

d = { i: object() for i in range(4) }

print(weekend)
print(vals)
print(capitals)
print(d)
```

In the example, we create four dictionaries in four different ways. Later we print the   
contents of these dictionaries to the console.

```python
weekend = { "Sun": "Sunday", "Mon": "Monday" }
```

We create a weekend dictionary using dictionary literal notation. The key-value pairs are  
enclosed by curly brackets. The pairs are separated by commas. The first value of a pair  
is a key, which is followed by a colon character and a value. The "Sun" string is a key  
and the "Sunday" string is a value.

```python
vals = dict(one=1, two=2)
```

Dictionaries can be created using the `dict` function.

```python
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
```

In the third way, an empty `capitals` dictionary is created and three pairs are added  
to it. The key goes inside the square brackets; the value goes on the right side of  
the assignment.

```python
d = { i: object() for i in range(4) }
```

A dictionary is created using a dictionary comprehension. The comprehension has two parts:  
the `i: object()` expression, which is evaluated on each iteration of the loop, and the  
`for i in range(4)` loop. It creates a dictionary with four pairs, where the keys are the  
numbers 0, 1, 2, and 3 and the values are simple objects.

```
$ ./create_dict.py
{'Sun': 'Sunday', 'Mon': 'Monday'}
{'one': 1, 'two': 2}
{'svk': 'Bratislava', 'deu': 'Berlin', 'dnk': 'Copenhagen'}
{0: <object object at 0xb76cb4a8>, 1: <object object at 0xb76cb4b0>,
2: <object object at 0xb76cb4b8>, 3: <object object at 0xb76cb4c0>}
```


## Basic operations

The following example shows some basic operations with dictionaries.

```python

# basics.py

basket = { 'oranges': 12, 'pears': 5, 'apples': 4 }

basket['bananas'] = 5

print(basket)
print("There are {0} various items in the basket".format(len(basket)))

print(basket['apples'])
basket['apples'] = 8
print(basket['apples'])

print(basket.get('oranges', 'undefined'))
print(basket.get('cherries', 'undefined'))
```

We have a basket with different fruits. We perform some operations on the basket  
dictionary.

```python
basket = { 'oranges': 12, 'pears': 5, 'apples': 4 }
```

The basket dictionary is created. It has initially three key-value pairs.

```python
basket['bananas'] = 5
```

A new pair is created. The `'bananas'` string is a key, the 5 integer is the value.

```python
print("There are {0} various items in the basket".format(len(basket)))
```

The len function gives the number of pairs in the dictionary.

```python
print(basket['apples'])
```

The value of the 'apples' key is printed to the terminal.

```python
basket['apples'] = 8
```

The value of the 'apples' key is modified. It is set to number 8.

```python
print(basket.get('oranges', 'undefined'))
```

The `get` method retrieves the value of a specified key. If there is no such key,  
the second parameter of the method is returned.

```python
print(basket.get('cherries', 'undefined'))
```

This line returns 'undefined'. There are no cherries in the basket.

```
$ ./basics.py
{'oranges': 12, 'pears': 5, 'apples': 4, 'bananas': 5}
There are 4 various items in the basket
4
8
12
undefined
```

## The fromkeys and setdefault methods

The next example presents two dictionary methods: `fromkeys` and `setdefault`.

```python

# fruits.py

basket = ('oranges', 'pears', 'apples', 'bananas')

fruits = dict.fromkeys(basket, 0)
print(fruits)

fruits['oranges'] = 12
fruits['pears'] = 8
fruits['apples'] = 4

print(fruits.setdefault('oranges', 11))
print(fruits.setdefault('kiwis', 11))

print(fruits)
```

The `fromkeys` method creates a new dictionary from a sequence of keys. The `setdefault`  
method returns a value if a key is present; otherwise, it inserts the key with a specified  
default value and returns that value.

```python
basket = ('oranges', 'pears', 'apples', 'bananas')
```

We have a tuple of strings. From this sequence a new dictionary will be constructed.

```python
fruits = dict.fromkeys(basket, 0)
```

The `fromkeys` method creates a new dictionary whose keys are the items of the sequence.  
Each key is initialized to 0. Since it is a class method, we call it via the `dict` class.

```python
fruits['oranges'] = 12
fruits['pears'] = 8
fruits['apples'] = 4
```

Here we add some values to the `fruits` dictionary.

```python
print(fruits.setdefault('oranges', 11))
print(fruits.setdefault('kiwis', 11))
```

The first line prints 12: the 'oranges' key exists in the dictionary, so the method  
returns its value. In the second case, the key does not exist yet; the method inserts  
the pair 'kiwis': 11 into the dictionary and returns 11.

```python
$ ./fruits.py
{'oranges': 0, 'pears': 0, 'apples': 0, 'bananas': 0}
12
11
{'oranges': 12, 'pears': 8, 'apples': 4, 'bananas': 0, 'kiwis': 11}
```

We receive this output when we launch the fruits.py script.

## The update method

The next code example shows how to add two Python dictionaries using the update method.

```python

# domains.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary"}
domains2 = { "us": "United States", "no": "Norway" }

domains.update(domains2)

print(domains)
```

Two dictionaries are joined with the update method.  

```python
domains.update(domains2)
```

The `domains2` dictionary is added to the domains dictionary with the `update` method.

```
$ ./domains.py
{'de': 'Germany', 'sk': 'Slovakia', 'hu': 'Hungary',
'us': 'United States', 'no': 'Norway'}
```

The result shows all values.

## Removing items from dictionary

Now we show how to remove a pair from a dictionary.

```python

# removing.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

print(items)

item = items.pop("coins")
print("Item having value {0} was removed".format(item))

print(items)

del items["bottles"]
print(items)

items.clear()
print(items)
```

The `items` dictionary has six key-value pairs. We will delete pairs from this dictionary.

```python
item = items.pop("coins")
print("Item having value {0} was removed".format(item))
```

The `pop` method removes a pair with a specified key; it returns the value of the removed key.

```
del items["bottles"]
```

The `del` keyword deletes the "bottles": 4 pair from the items dictionary.

```python
items.clear()
```

The `clear` method clears all items from the dictionary.

```
$ ./removing.py
{'coins': 7, 'pens': 3, 'cups': 2, 'bags': 1, 'bottles': 4, 'books': 5}
Item having value 7 was removed
{'pens': 3, 'cups': 2, 'bags': 1, 'bottles': 4, 'books': 5}
{'pens': 3, 'cups': 2, 'bags': 1, 'books': 5}
{}
```

## Dictionary keys and values

A Python dictionary consists of key-value pairs. The `keys`, `values`, and `items` methods  
return views of the dictionary's keys, values, and key-value tuples. A view can be iterated  
over or converted to a list.

```python

# keys_values.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway"  }

print(domains.keys())
print(domains.values())
print(domains.items())

print("de" in domains)
print("cz" in domains)
```

We demonstrate the above mentioned methods. We also check if a key is present with  
the `in` keyword.

```python
print(domains.keys())
```

We print the keys of the domains dictionary with the `keys` method.

```python
print(domains.values())
```

We print the values of the domains dictionary with the `values` method.

```python
print(domains.items())
```

And finally, we print the key-value tuples with the `items` method.

```python
print("de" in domains)
print("cz" in domains)
```

With the in keyword, we check if the "de", "cz" keys are present in the domains dictionary. 
The return value is either `True` or `False`.

```
$ ./keys_values.py
dict_keys(['de', 'sk', 'hu', 'us', 'no'])
dict_values(['Germany', 'Slovakia', 'Hungary', 'United States', 'Norway'])
dict_items([('de', 'Germany'), ('sk', 'Slovakia'), ('hu', 'Hungary'),
('us', 'United States'), ('no', 'Norway')])
True
False
```

## Looping

Looping through a dictionary is a common task, done with the `for` keyword.

```python

# looping.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway" }

for key in domains:
    print(key)

for val in domains.values():
    print(val)

for k, v in domains.items():
    print(": ".join((k, v)))
```

In the example, we traverse the domains dictionary to print the keys, values and both keys  
and values of the dictionary.

```python
for key in domains:
    print(key)
```

This loop prints all the keys of the dictionary.

```python
for val in domains.values():
    print(val)
```

The second loop prints all values of the dictionary.

```python
for k, v in domains.items():
    print(": ".join((k, v)))
```

In the third loop, all keys and values are printed.

```
$ ./looping.py
de
sk
hu
us
no
Germany
Slovakia
Hungary
United States
Norway
de: Germany
sk: Slovakia
hu: Hungary
us: United States
no: Norway
```

## Dictionary membership testing

With the `in` and `not in` operators, we can check if a key is present in a dictionary.

```python

# membership.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway"  }

key = "sk"

if key in domains:
    print("{0} is in the dictionary".format(domains[key]))
```

In the example, we check whether the `sk` key is present in the dictionary with the `in` operator.

## defaultdict

A `defaultdict` is a dictionary subclass that automatically supplies a default value for  
keys that do not exist. It eliminates the need to check for a key's presence before  
accessing or modifying it.

The `defaultdict` is defined in the standard `collections` module:

```python
from collections import defaultdict
```

We create a `defaultdict` by passing a callable (such as `int`, `list`, or `set`) to its  
constructor. When a missing key is accessed, the callable is invoked and its return value  
becomes the default value for the key.

Common default factories include:

- `int`: For numeric counters or accumulators
- `list`: For storing multiple values under one key
- `dict`: For building nested dictionaries
- `set`: For collecting unique values

Counting letters with a plain dictionary:

```python
msg = 'there is an old falcon in the sky'

chars = {}

for c in msg:

    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1

print(chars)
```

Counting letters with a `defaultdict`:

```python
from collections import defaultdict

msg = 'there is an old falcon in the sky'

chars = defaultdict(int)

for c in msg:

    chars[c] += 1

for k in chars:
    print(k, chars[k])
```


## Sorting

Since Python 3.7, dictionaries preserve insertion order. This means the order in which  
key-value pairs are added to the dictionary is kept when iterating over it.

We might want to sort the data in a normal or reverse order. We can sort the data by keys  
or by values.

```python

# simple_sort.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

kitems = list(items.keys())
kitems.sort()

for k in kitems:
    print(": ".join((k, str(items[k]))))
```

The first example shows the simplest way to sort the data by keys.

```python
kitems = list(items.keys())
kitems.sort()
```

A list of keys is obtained from the dictionary and sorted with the `sort` method.

```python
for k in kitems:
    print(": ".join((k, str(items[k]))))
```

In the loop we print the sorted keys together with their values from the dictionary.

```
$ ./simple_sort.py
bags: 1
books: 5
bottles: 4
coins: 7
cups: 2
pens: 3
```

The items dictionary is sorted by its keys.

More efficient sorting can be done with the built-in `sorted` function.

```python

# sorting.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

for key in sorted(items.keys()):
    print("{0}: {1}".format(key, items[key]))

print("###############")

for key in sorted(items.keys(), reverse=True):
    print("{0}: {1}".format(key, items[key]))
```

In the example we print sorted data by their keys in ascending and descending  
order using the sorted function.

```python
for key in sorted(items.keys()):
    print("{0}: {1}".format(key, items[key]))
```

In this for loop, we print the pairs sorted in ascending order by keys.

```python
for key in sorted(items.keys(), reverse=True):
    print("{0}: {1}".format(key, items[key]))
```

In the second for loop, the data is sorted in descending order. The order type is  
controlled by the `reverse` parameter.

```
$ ./sorting.py
bags: 1
books: 5
bottles: 4
coins: 7
cups: 2
pens: 3
###############
pens: 3
cups: 2
coins: 7
bottles: 4
books: 5
bags: 1
```

In the next example, we are going to sort the items by their values.

```python

# sorting2.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

for key, value in sorted(items.items(), key=lambda pair: pair[1]):

    print("{0}: {1}".format(key, value))

print("###############")

for key, value in sorted(items.items(), key=lambda pair: pair[1], reverse=True):

    print("{0}: {1}".format(key, value))
```

The example prints the data in ascending and descending order by their values.  

```python
for key, value in sorted(items.items(), key=lambda pair: pair[1]):
    print("{0}: {1}".format(key, value))
```

Dictionary pairs are sorted by their values and printed to the console. The `key` parameter  
takes a function which determines the sort order.

```
$ ./sorting2.py
bags: 1
cups: 2
pens: 3
bottles: 4
books: 5
coins: 7
###############
coins: 7
books: 5
bottles: 4
pens: 3
cups: 2
bags: 1
```

From the output we can see that this time the pairs were sorted by their values.


## Dictionary comprehension

A dictionary comprehension is a syntactic construct which creates a dictionary based on  
an existing dictionary.

```python
D = { key: value for variable in sequence [if condition] }
```

A dictionary comprehension is placed between two curly brackets; it consists of a for  
loop, an optional condition, and a key-value expression.

The for loop iterates over the input sequence. The optional `if` condition filters the  
items; only those that satisfy it are kept. For each remaining item, the expression is  
evaluated and produces a key-value pair of the new dictionary.

```python

# comprehension.py

capitals = { "Bratislava": 424207, "Vilnius": 556723, "Lisbon": 564657,
             "Riga": 713016, "Jerusalem": 780200, "Warsaw": 1711324,
             "Budapest": 1729040, "Prague": 1241664, "Helsinki": 596661,
             "Tokyo": 13189000, "Madrid": 3233527 }


capitals2 = { key: val for key, val in capitals.items() if val < 1000000 }

print(capitals2)
```

In the example, we create a new dictionary from an existing dictionary.

```python
capitals = { "Bratislava": 424207, "Vilnius": 556723, "Lisbon": 564657,
             "Riga": 713016, "Jerusalem": 780200, "Warsaw": 1711324,
             "Budapest": 1729040, "Prague": 1241664, "Helsinki": 596661,
             "Tokyo": 13189000, "Madrid": 3233527 }
```

We have a dictionary of capitals. The capital is the key and the population is the value.

```python
capitals2 = { key: val for key, val in capitals.items() if val < 1000000 }
```

A new dictionary is created using a dictionary comprehension. It contains capitals  
that have a population smaller than one million.

```
$ ./comprehension.py
{'Bratislava': 424207, 'Vilnius': 556723, 'Lisbon': 564657, 'Riga': 713016,
    'Jerusalem': 780200, 'Helsinki': 596661}
```

These capitals have a population smaller than one million.

