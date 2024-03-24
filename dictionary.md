# Dictionary

A *Python dictionary* is a container of key-value pairs. It is mutable and can contain mixed   
types. A dictionary is an unordered collection. Python dictionaries are called associative   
arrays or hash tables in other languages. The keys in a dictionary must be immutable objects   
like strings or numbers. They must also be unique within a dictionary.  

## Creation

First, we show how to create Python dictionaries.

```python
#!/usr/bin/python

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

Dictionaries can be created using the dict function.

```python
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
```

In the third way an empty capitals dictionary is created. Three pairs are added to the  
dictionary. The keys are inside the square brackets, the values are located on the right  
side of the assignment.

```python
d = { i: object() for i in range(4) }
```

A dictionary is created using a dictionary comprehension. The comprehension has two parts.  
The first part is the `i:` object expression, which is executed for each cycle of a loop.  
The second part is the `for i in range(4)` loop. The dictionary comprehension creates a dictionary  
having four pairs, where the keys are numbers 0, 1, 2, and 3 and the values are simple objects.

```
$ ./create_dict.py
{'Sun': 'Sunday', 'Mon': 'Monday'}
{'two': 2, 'one': 1}
{'svk': 'Bratislava', 'dnk': 'Copenhagen', 'deu': 'Berlin'}
{0: <object object at 0xb76cb4a8>, 1: <object object at 0xb76cb4b0>,
2: <object object at 0xb76cb4b8>, 3: <object object at 0xb76cb4c0>}
```

## Dictionary comprehension

A dictionary comprehension is a syntactic construct which creates a dictionary based on  
existing dictionary.

```python
D = { expression for variable in sequence [if condition] }
```

A dictionary comprehension is placed between two curly brackets; it has three parts:  
for loop, condition, and expression.

In the for loop, we go through the dictionary. The optional if condition specifies a  
condition which must be met. In the end, the expression is evaluated. The expression  
produces elements of the output dictionary from members of the input sequence that  
satisfy the condition.

```python
#!/usr/bin/python

# comprehension.py

capitals = { "Bratislava": 424207, "Vilnius": 556723, "Lisbon": 564657,
             "Riga": 713016, "Jerusalem": 780200, "Warsaw": 1711324,
             "Budapest": 1729040, "Prague": 1241664, "Helsinki": 596661,
             "Yokyo": 13189000, "Madrid": 3233527 }


capitals2 = { key:val for key, val in capitals.items() if val < 1000000 }

print(capitals2)
```

In the example, we create a new dictionary from an existing dictionary.

```python
capitals = { "Bratislava": 424207, "Vilnius": 556723, "Lisbon": 564657,
             "Riga": 713016, "Jerusalem": 780200, "Warsaw": 1711324,
             "Budapest": 1729040, "Prague": 1241664, "Helsinki": 596661,
             "Yokyo": 13189000, "Madrid": 3233527 }
```

We have a dictionary of capitals. The capital in a key and the population is  
the value.

```python
capitals = { key:val for key, val in capitals.items() if val < 1000000 }
```

A new dictionary is created using a dictionary comprehension. It contains capitals  
that have a population smaller than one million.

```
$ ./comprehension.py
{'Bratislava': 424207, 'Vilnius': 556723, 'Jerusalem': 780200, 'Riga': 713016,
    'Lisbon': 564657, 'Helsinki': 596661}
```

These capitals have a population smaller than one million.

## Basic operations

The following examples shows some basic operations with dictionaries.

```python
#!/usr/bin/python

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

The `get` method retrieves the value of a specified key. If there is no   
such a key, the second parameter of the method is returned.

```python
print(basket.get('cherries', 'undefined'))
```

This line returns 'undefined'. There are no cherries in the basket.

```
$ ./basics.py
{'bananas': 5, 'pears': 5, 'oranges': 12, 'apples': 4}
There are 4 various items in the basket
4
8
12
undefined
```

## The fromkeys and setdefault methods

The next example presents two dictionary methods: `fromkeys` and `setdefault`.

```python
#!/usr/bin/python

# fruits.py

basket = ('oranges', 'pears', 'apples', 'bananas')

fruits = {}.fromkeys(basket, 0)
print(fruits)

fruits['oranges'] = 12
fruits['pears'] = 8
fruits['apples'] = 4

print(fruits.setdefault('oranges', 11))
print(fruits.setdefault('kiwis', 11))

print(fruits)
```

The `fromkeys` method creates a new dictionary from a list. The setdefault method  
returns a value if a key is present. Otherwise, it inserts a key with a specified default  
value and returns the value.

```python
basket = ('oranges', 'pears', 'apples', 'bananas')
```

We have a list of strings. From this list a new dictionary will be constructed.

```python
fruits = {}.fromkeys(basket, 0)
```

The `fromkeys` method creates a new dictionary, where the list items will be the keys.  
Each key will be initiated to 0. Note that the fromkeys method is a class method and  
needs the class name, which is `{}` in our case, to be called.

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

The first line prints 12 to the terminal. The 'oranges' key exists in the dictionary.  
In such a case, the method returns the its value. In the second case, the key does  
not exist yet. A new pair 'kiwis': 11 is inserted to the dictionary. And value 11 is  
printed to the console.

```python
$ ./fruits.py
{'bananas': 0, 'pears': 0, 'oranges': 0, 'apples': 0}
12
11
{'kiwis': 11, 'bananas': 0, 'pears': 8, 'oranges': 12, 'apples': 4}
```

We receive this output when we launch the fruits.py script.

## The update method

The next code example shows how to add two Python dictionaries using the update method.

```python
#!/usr/bin/python

# domains.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary"}
domains2 = { "us": "United States", "no": "Norway" }

domains.update(domains2)

print(domains)
Two dictionaries are joined with the update method.

domains.update(domains2)
```

The `domains2` dictionary is added to the domains dictionary with the `update` method.

```
$ ./domains.py
{'sk': 'Slovakia', 'de': 'Germany', 'no': 'Norway',
'us': 'United States', 'hu': 'Hungary'}
```

The result shows all values.

## Removing items from dictionary

Now we show how to remove a pair from a dictionary.

```python
#!/usr/bin/python

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
{'bags': 1, 'pens': 3, 'coins': 7, 'books': 5, 'bottles': 4, 'cups': 2}
Item having value 7 was removed
{'bags': 1, 'pens': 3, 'books': 5, 'bottles': 4, 'cups': 2}
{'bags': 1, 'pens': 3, 'books': 5, 'cups': 2}
{}
```

## Dictionary keys and values

A Python dictionary consists of key-value pairs. The keys method returns a list of keys  
from a dictionary. The values method creates a list of values. And the items method returns  
a list of key-value tuples.

```python
#!/usr/bin/python

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

We print the list of keys of a domains dictionary with the keys method.

```python
print(domains.values())
```

We print the list of values of a domains dictionary with the `values` method.

```python
print(domains.items())
```

And finally, we print the list of key-value tuples of a domains dictionary using  
the `items` method.

```python
print("de" in domains)
print("cz" in domains)
```

With the in keyword, we check if the "de", "cz" keys are present in the domains dictionary. The return value is either True or False.

```
$ ./keys_values.py
['sk', 'de', 'no', 'us', 'hu']
['Slovakia', 'Germany', 'Norway', 'United States', 'Hungary']
[('sk', 'Slovakia'), ('de', 'Germany'), ('no', 'Norway'),
('us', 'United States'), ('hu', 'Hungary')]
True
False
```

# Loooping

Looping through the dictionary is a common programming job. This can be done with the `for` keyword. 

```python
#!/usr/bin/python

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
sk
de
no
us
hu
Slovakia
Germany
Norway
United States
Hungary
sk: Slovakia
de: Germany
no: Norway
us: United States
hu: Hungary
```

## Dictionary membership testing

With the in and not in operators we can check if an key is present in a dictionary.

```python
#!/usr/bin/python

# membership.py

domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
    "us": "United States", "no": "Norway"  }

key = "sk"

if key in domains:
    print("{0} is in the dictionary".format(domains[key]))
```

In the example we check if a country is in the dictionary with the in operator.

## Sorting

Python dictionaries are orderless. This also implies that they cannot be sorted like a  
Python list. Programmers can create sorted representations of Python dictionaries.  
In this section, we show several ways to create a sorted output.

Programmers might want to sort the data in a normal or reverse order. They could sort  
the data by keys or by values.

```python
#!/usr/bin/python

# simple_sort.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

kitems = list(items.keys())
kitems.sort()

for k in kitems:
    print(": ".join((k, str(items[k]))))
```

The first example provides the simplest solution to have the data sorted by the keys.

```python
kitems = items.keys()
kitems.sort()
```

A list of keys is obtained from the dictionary. The list is sorted with the `sort` method.

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
#!/usr/bin/python

# sorting.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

for key in sorted(items.keys()):
    print("%{0}: {1}".format(key, items[key]))

print("###############")

for key in sorted(items.keys(), reverse=True):
    print("{0}: {1}".format(key, items[key]))
```

In the example we print sorted data by their keys in ascending and descending  
order using the sorted function.

```python
for key in sorted(items.keys()):
    print("%{0}: {1}".format(key, items[key]))
```

In this for loop, we print the pairs sorted in ascending order. The `iteritems`  
function returns an iterator over the dictionary's (key, value) pairs.

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
#!/usr/bin/python

# sorting2.py

items = { "coins": 7, "pens": 3, "cups": 2,
    "bags": 1, "bottles": 4, "books": 5 }

for key, value in sorted(items.items(), key=lambda pair: pair[1]):

    print("{0}: {1}".format(key, value))

print("###############")

for key, value in sorted(items.items(), key=lambda pair: pair[1], reverse=True):

    print("{0}: {1}".format(key, value))
The example prints the data in ascending and descending order by their values.

for key, value in sorted(items.iteritems(),
    key=lambda (k,v): (v,k)):
```

Dictionary pairs are sorted by their values and printed to the console. The key parameter  
takes a function which indicates how the data is going to be sorted.

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
