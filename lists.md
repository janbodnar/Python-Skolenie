# Lists


A *list* is an ordered collection of values. It can contain various types of values. A list is a mutable  
container. This means that we can add values, delete values, or modify existing values. 

Python list represents a mathematical concept of a finite sequence. Values of a list are called items or  
elements of the list. A list can contain the same value multiple times. Each occurrence is considered a distinct item. 

## Simple example 

List elements can be accessed by their index. The first element has index 0, the last one has index -1.

```python
#!/usr/bin/python

# simple.py

nums = [1, 2, 3, 4, 5]

print(nums[0])
print(nums[-1])
print(nums)
```

This is a simple list having five elements. The list is delimited by square brackets `[]`.  
The elements of a list are separated by a comma character. The contents of a list are printed to the console.  

```python
nums = [1, 2, 3, 4, 5]
```

The right side of the assignment is a Python list literal. It creates a list containing five elements.  

```
$ ./simple.py
1
5
[1, 2, 3, 4, 5]
```

Lists can contain elements of various data types.

```python
#!/usr/bin/python

# various_types.py

class Being:
    pass

objects = [1, -2, 3.4, None, False, [1, 2], "Python", (2, 3), Being(), {}]
print(objects)
```

In the example, we create an objects list. It contains numbers, a boolean value, another list,  
a string, a tuple, a custom object, and a dictionary. 

```
$ ./various_types.py
[1, -2, 3.4, None, False, [1, 2], 'Python', (2, 3),
    <__main__.Being instance at 0x7f653577f6c8>, {}]
```

## List initialization

Sometimes we need to initialize a list in advance to have a particular number of elements.

```python
#!/usr/bin/python

# initialization.py

n1 = [0 for i in range(15)]
n2 = [0] * 15

print(n1)
print(n2)

n1[0:10] = [10] * 10

print(n1)
```

In this example we initialize two lists using a list comprehension and a `*` operator.  

```
n1 = [0 for i in range(15)]
n2 = [0] * 15
```

These two lists are initialized to fifteen zeros.

```python
n1[0:10] = [10] * 10
```

First ten values are replaced with 10s.

```
$ ./initialization.py
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0]
```

## The list function

The list function creates a list from an iterable object. An iterable may be either a sequence,  
a container that supports iteration, or an iterator object. If no parameter is specified,  
a new empty list is created.

```python
#!/usr/bin/python

# list_fun.py

a = []
b = list()

print(a == b)

print(list((1, 2, 3)))
print(list("ZetCode"))
print(list(['Ruby', 'Python', 'Perl']))
```

In the example, we create an empty list, a list from a tuple, a string, and another list.

```python
a = []
b = list()
```

These are two ways to create an empty list.

```python
print(a == b)
```

The line prints `True`. This confirms that a and b are equal.

```python
print(list((1, 2, 3)))
```

We create a list from a Python tuple.

```python
print(list("ZetCode"))
```

This line produces a list from a string.

```python
print(list(['Ruby', 'Python', 'Perl']))
```

Finally, we create a copy of a list of strings.

```
$ ./list_fun.py
True
[1, 2, 3]
['Z', 'e', 't', 'C', 'o', 'd', 'e']
['Ruby', 'Python', 'Perl']
```

## List operations

The following code shows some basic list operations.

```python
#!/usr/bin/python

# list_oper.py

n1 = [1, 2, 3, 4, 5]
n2 = [3, 4, 5, 6, 7]

print(n1 == n2)
print(n1 + n2)

print(n1 * 3)

print(2 in n1)
print(2 in n2)
```

We define two lists of integers. We use a few operators on these lists.

```python
print(n1 == n2)
```

The contents of the lists are compared with the `==` operator. The line prints  
`False` since the elements are different.

```python
print(n1 + n2)
```

The `n1` and `n2` lists are added to form a new list. The new list has all elements  
of both the lists.

```python
print(n1 * 3)
```

We use the multiplication operator on the list. It repeats the elements n times;  
three times in our case.

```python
print(2 in n1)
```

We use the in operator to find out whether the value is present in the list. It returns  
a boolean `True` or `False`.

```
$ ./lists.py
False
[1, 2, 3, 4, 5, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
True
False
```

## Sequence functions

Sequence functions can be used on any sequence types, including lists.

```python
#!/usr/bin/python

# sequence_funs.py

n = [1, 2, 3, 4, 5, 6, 7, 8]

print("There are {0} items".format(len(n)))
print("Maximum is {0}".format(max(n)))
print("Minimum is {0}".format(min(n)))
print("The sum of values is {0}".format(sum(n)))
```

In the example above, we have four functions: `len`, `max`, `min`, and `sum`.

```python
print("There are {0} items".format(len(n)))
```

The `len` function returns the size of the list. The number of elements of the list.

```python
print("Maximum is {0}".format(max(n)))
print("Minimum is {0}".format(min(n)))
```

The `max` and `min` functions return the maximum and the minimum of the list.

```python
print("The sum of values is {0}".format(sum(n)))
```

The `sum` function calculates the sum of the numbers of the `n` list.

```
$ ./sequence_funs.py
There are 8 items
Maximum is 8
Minimum is 1
The sum of values is 36
```

## Adding list elements

This section shows how elements are added to a Python list.

```python
#!/usr/bin/python

# adding.py

langs = []

langs.append("Python")
langs.append("Perl")
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)

langs.extend(("JavaScript", "ActionScript"))
print(langs)
```

We have three methods to add new elements to a list: `append`, `insert`, and `extend`.

```python
langs = []
```

An empty list is created.

```python
langs.append("Python")
langs.append("Perl")
```

The `append` method adds an item at the end of the list; we append two strings.

```python
langs.insert(0, "PHP")
langs.insert(2, "Lua")
```

The `insert` method places an element at a specific position indicated by the index number.  
The "PHP" string is inserted at the first position, the "Lua" string at the third position.  
Note that list index numbers start from zero.  

```python
langs.extend(("JavaScript", "ActionScript"))
```

The `extend` method adds a sequence of values to the end of a list. In our case two strings  
of a Python tuple are appended at the end of our list.

```
$ ./adding.py
['Python', 'Perl']
['PHP', 'Python', 'Lua', 'Perl']
['PHP', 'Python', 'Lua', 'Perl', 'JavaScript', 'ActionScript']
```

## List IndexError

The `IndexError` is raised when a list subscript is out of range.

```python
#!/usr/bin/python

# index_error.py

n = [1, 2, 3, 4, 5]

try:

    n[0] = 10
    n[6] = 60

except IndexError as e:

    print(e)
```

In the script we have defined a list of five integers. These elements have indexes 0, 1, 2, 3, and 4.  
Using a bigger index leads to an error.

```python
n[6] = 60
```

Index 6 is out of range for our list. An `IndexError` is thrown.

```python
except IndexError as e:

    print(e)
```

We catch the error using the except clause. In the body of the clause, we print the error message.  

```
$ ./index_error.py
list assignment index out of range
```

## TypeError

If an index of a tuple is not a plain integer a TypeError is thrown.  

```python
#!/usr/bin/python

# type_error.py

n = [1, 2, 3, 4, 5]

try:
    print(n[1])
    print(n['2'])

except TypeError as e:

    print("Error in file {0}".format( __file__))
    print("Message: {0}".format(e))
```

This example throws a `TypeError`.

```python
print(n['2'])
```

A list index must be an integer. Other types end in error.

```python
except TypeError as e:

    print("Error in file {0}".format( __file__))
    print("Message: {0}".format(e))
```

In the except block, we print the name of the file, where the exception has occurred  
and the message string.

```
$ ./typeerror.py
2
Error in file ./typeerror.py
Message: list indices must be integers, not str
```

## Remove elements

Previously we have added items to a list. Now we be removing them from a list.

```python
#!/usr/bin/python

# removing.py

langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript"]
print(langs)

lang = langs.pop(3)
print("{0} was removed".format(lang))

lang = langs.pop()
print("{0} was removed".format(lang))

print(langs)

langs.remove("Ruby")
print(langs)
```

The `pop` method removes and returns an element with a specified index or the last  
element if the index number is not given. The remove method removes a particular item from a list. 

```python
lang = langs.pop(3)
print("{0} was removed".format(lang))
```

We take away the element which has index 3. The `pop` method returns the name of the removed element;  
it is printed to the console.

```python
lang = langs.pop()
print("{0} was removed".format(lang))
```

The last element from the list, namely "JavaScript" string, is removed from the list.

```python
langs.remove("Ruby")
```

This line removes a "Ruby" string from the langs list.

```
['Python', 'Ruby', 'Perl', 'Lua', 'JavaScript']
Lua was removed
JavaScript was removed
['Python', 'Ruby', 'Perl']
['Python', 'Perl']
```

From the ouput of the script we can see the effects of the described methods.  

A `del` keyword can be used to delete list elements as well.

```python
#!/usr/bin/python

# removing2.py

langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript"]
print(langs)

del langs[1]
print(langs)

#del langs[15]

del langs[:]
print(langs)
```

We have a list of strings. We use the del keyword to delete list elements.

```python
del langs[1]
```

We remove the second string from the list. It is the "Ruby" string.  

```python
#del langs[15]
```

We can delete only existing elements. If we uncomment the code line, we receive an `IndexError` message.

```python
del langs[:]
```

Here we remove all the remaining elements from the list. The `[:]` characters refer to all items of a list.

```
$ ./removing2.py
['Python', 'Ruby', 'Perl', 'Lua', 'JavaScript']
['Python', 'Perl', 'Lua', 'JavaScript']
[]
```

## Modify list elements

In the next example we be modifying list elements.

```python
#!/usr/bin/python

# modifying.py

langs = ["Python", "Ruby", "Perl"]

langs.pop(2)
langs.insert(2, "PHP")
print(langs)

langs[2] = "Perl"
print(langs)
```

In the example we modify the third element of the langs list twice.

```python
langs.pop(2)
langs.insert(2, "PHP")
```

One way to modify an element is to remove it and place a different element at the same position.

```python
langs[2] = "Perl"
```

The other method is more straightforward. We assign a new element at a given position. Now there is  
"Perl" string at the third position again.

```
$ ./modifying.py
['Python', 'Ruby', 'PHP']
['Python', 'Ruby', 'Perl']
```

## Copy list

There are several ways how we can copy a list in Python. We mention a few of them.

```python
#!/usr/bin/python

# copying.py

import copy

w = ["Python", "Ruby", "Perl"]

c1 = w[:]
c2 = list(w)
c3 = copy.copy(w)
c4 = copy.deepcopy(w)
c5 = [e for e in w]

c6 = []

for e in w:
    c6.append(e)

c7 = []
c7.extend(w)

print(c1, c2, c3, c4, c5, c6, c7)
```

We have a list of three strings. We make a copy of the list seven times.

```python
import copy
```

We import the copy module which has two methods for copying.  

```python
c1 = w[:]
```

A list is copied using the slice syntax.  

```python
c2 = list(w)
```

The list function creates a copy of a list when it takes a list as a parameter.

```python
c3 = copy.copy(w)
c4 = copy.deepcopy(w)
```

The `copy` method produces a shallow copy of a list. The `deepcopy` produces a deep copy of a list.

```python
c5 = [e for e in w]
```

A copy of a string is created using list comprehension.

```python
c6 = []

for e in w:
    c6.append(e)
A copy created by a for loop.

c7 = []
c7.extend(w)
```

The `extend` method can be used to create a copy too.

```
$ ./copying.py
['Python', 'Ruby', 'Perl'] ['Python', 'Ruby', 'Perl'] ['Python', 'Ruby', 'Perl']
['Python', 'Ruby', 'Perl'] ['Python', 'Ruby', 'Perl'] ['Python', 'Ruby', 'Perl']
['Python', 'Ruby', 'Perl']
```

Seven copies of a string list were created using different techniques.

## Indexing list elements

Elements in a Python list can be accessed by their index. Index numbers are integers;  
they start from zero. Indexes can be negative; negative indexes refer to elements from  
the end of the list. The first item in a list has index 0, the last item has -1. 

```python
#!/usr/bin/python

# indexing.py

n = [1, 2, 3, 4, 5, 6, 7, 8]

print(n[0])
print(n[-1])
print(n[-2])

print(n[3])
print(n[5])
```

We can access an element of a list by its index. The index is placed between the square   
brackets `[]` after the name of the list.

```python
print(n[0])
print(n[-1])
print(n[-2])
```

These three lines print the first, the last and the last but one item of the list.  

```python
print(n[3])
print(n[5])
```

The two lines print the fourth and sixth element of the list.  

```python
$ ./indexing.py
1
8
7
4
6
```

The `index(e, start, end)` method looks for a particular element and returns its lowest index.  
The start and end are optional parameters that limit the search to given boundaries.  

```python
#!/usr/bin/python

# indexing2.py

n = [1, 2, 3, 4, 1, 2, 3, 1, 2]

print(n.index(1))
print(n.index(2))

print(n.index(1, 1))
print(n.index(2, 2))

print(n.index(1, 2, 5))
print(n.index(3, 4, 8))
```

A code example with the index method.

```python
print(n.index(1))
print(n.index(2))
```

These two lines print the indexes of the leftmost 1, 2 values of the n list.

```python
print(n.index(1, 1))
print(n.index(2, 2))
```

Here we search for values 1 and 2 after specified indexes.  

```python
print(n.index(1, 2, 5))
```

Here we search for value 1 between values with indexes 2 and 5.  

```python
$ ./indexing2.py
0
1
4
5
4
6
```

## List slice

List slicing is an operation that extracts certain elements from a list and forms them into another list.  
Possibly with different number of indices and different index ranges.

The syntax for list slicing is as follows:  

```
[start:end:step]
```

The start, end, step parts of the syntax are integers. Each of them is optional. They can be both positive  
and negative. The value having the end index is not included in the slice. 

```python
#!/usr/bin/python

# slice.py

n = [1, 2, 3, 4, 5, 6, 7, 8]

print(n[1:5])
print(n[:5])
print(n[1:])
print(n[:])
```

We create four slices from a list of eight integers. 

```python
print(n[1:5])
```

The first slice has values with indexes 1, 2, 3, and 4. The newly formed list is `[2, 3, 4, 5]`.  

```python
print(n[:5])
```

If the start index is omitted then a default value is assumed, which is 0. The slice is `[1, 2, 3, 4, 5]`.

```python
print(n[1:])
```

If the end index is omitted, the -1 default value is taken. In such a case a slice takes all  
values to the end of the list.

```python
print(n[:])
```

Even both indexes can be left out. This syntax creates a copy of a list.

```
$ ./slice.py
[2, 3, 4, 5]
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
```

The third index in a slice syntax is the step. It allows us to take every n-th value from a list.

```python
#!/usr/bin/python

# slice2.py

n = [1, 2, 3, 4, 5, 6, 7, 8]

print(n[1:9:2])
print(n[::2])
print(n[::1])
print(n[1::3])
```

We form four new lists using the step value.

```python
print(n[1:9:2])
```

Here we create a slice having every second element from the n list, starting from the second element,  
ending in the eighth element. The new list has the following elements: `[2, 4, 6, 8]`.

```python
print(n[::2])
```

Here we build a slice by taking every second value from the beginning to the end of the list.  

```python
print(n[::1])
```

This creates a copy of a list.

```python
print(n[1::3])
```

The slice has every third element, starting from the second element to the end of the list.  

```python
$ ./slice2.py
[2, 4, 6, 8]
[1, 3, 5, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
[2, 5, 8]
```

Indexes can be negative numbers. Negative indexes refer to values from the end of the list.  
The last element has index -1, the last but one has index -2 etc. Indexes with lower negative numbers  
must come first in the syntax. This means that we write [-6, -2] instead of [-2, -6].  
The latter returns an empty list.  

```python
#!/usr/bin/python

# slice3.py

n = [1, 2, 3, 4, 5, 6, 7, 8]

print(n[-4:-1])
print(n[-1:-4])

print(n[-5:])
print(n[-6:-2:2])
print(n[::-1])
```

In this script, we form five lists. We also use negative index numbers.

```python
print(n[-4:-1])
print(n[-1:-4])
```

The first line returns `[5, 6, 7]`, the second line returns an empty list. Lower indexes must come before higher indexes.

```python
print(n[::-1])
```

This creates a reversed list.

```python
$ ./slice3.py
[5, 6, 7]
[]
[4, 5, 6, 7, 8]
[3, 5]
[8, 7, 6, 5, 4, 3, 2, 1]
```

The above mentioned syntax can be used in assignments. There must be an iterable on the right side of the assignment.

```python
#!/usr/bin/python

# slice4.py

n = [1, 2, 3, 4, 5, 6, 7, 8]

n[0] = 10
n[1:3] = 20, 30
n[3::1] = 40, 50, 60, 70, 80

print(n)
```

We have a list of eight integers. We use the slice syntax to replace the elements with new values.


## Loop list

This section will point out three basic ways to traverse a list in Python.

```python
#!/usr/bin/python

# traverse.py

n = [1, 2, 3, 4, 5]

for e in n:
    print(e, end=" ")

print()
```

The first one is the most straightforward way to traverse a list.

```python
n = [1, 2, 3, 4, 5]
```

We have a numerical list. There are five integers in the list.

```python
for e in n:
    print(e, end=" ")
```

Using the for loop, we go through the list one by one and print the current element to the console.

```
$ ./traverse.py
1 2 3 4 5
```

This is the output of the script. The integers are printed to the terminal.  

The second example is a bit more verbose.  

```python
#!/usr/bin/python

# traverse2.py

n = [1, 2, 3, 4, 5]

i = 0
s = len(n)

while i < s:

    print(n[i], end=" ")
    i = i + 1

print()
```

We are traversing the list using the while loop.

```python
i = 0
l = len(n)
```

First, we need to define a counter and find out the size of the list.

```python
while i < s:

    print(n[i], end=" ")
    i = i + 1
```

With the help of these two numbers, we go through the list and print each element to the terminal.  

The enumerate built-in function gives us both the index and the value of a list in a loop.  

```python
#!/usr/bin/python

# traverse3.py

n = [1, 2, 3, 4, 5]

print(list(enumerate(n)))

for e, i in enumerate(n):
    print("n[{0}] = {1}".format(e, i))
```

In the example, we print the values and the indexes of the values.  

```
$ ./traverse3.py
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
n[0] = 1
n[1] = 2
n[2] = 3
n[3] = 4
n[4] = 5
```

## Count list elements

Sometimes it is important to count list elements. For this, Python has the `count` method.

```python
#!/usr/bin/python

# counting.py

n = [1, 1, 2, 3, 4, 4, 4, 5]

print(n.count(4))
print(n.count(1))
print(n.count(2))
print(n.count(6))
```

In this example, we count the number of occurrences of a few numbers in the n list.

```python
n = [1, 1, 2, 3, 4, 4, 4, 5]
```

We have a list of integer numbers. Integers 1 and 4 are present multiple times.  

```python
print(n.count(4))
print(n.count(1))
print(n.count(2))
print(n.count(6))
```

Using the count method, we find out the occurrence of 4, 1, 2, and 6 numbers.  

```python
$ ./counting.py
3
2
1
0
```

Number 4 is present 3 times, 1 twice, 2 once, and 6 is not present in the list.  

## Nested lists

It is possible to nest lists into another lists. With a nested list a new dimension   
is created. To access nested lists one needs additional square brackets `[]`. 

```python
#!/usr/bin/python

# nested.py

nums = [[1, 2], [3, 4], [5, 6]]

print(nums[0])
print(nums[1])
print(nums[2])

print(nums[0][0])
print(nums[0][1])

print(nums[1][0])
print(nums[2][1])

print(len(nums))
```

In the example, we have three nested lists having two elements each.

```python
print(nums[0])
print(nums[1])
print(nums[2])
```

Three nested lists of the nums list are printed to the console.

```python
print(nums[0][0])
print(nums[0][1])
```

Here we print the two elements of the first nested list. The `nums[0]` refers to the first nested list;  
the `nums[0][0]` refers to the first element of the first nested list, namely 1.

```python
print(len(nums))
```

The line prints 3. Each nested list is counted as one element. Its inner elements are not taken into account.

```
$ ./nested.py
[1, 2]
[3, 4]
[5, 6]
1
2
3
6
3
```

The second example has additional dimensions.

```python
#!/usr/bin/python

# nested2.py

nums = [[1, 2, [3, 4, [5, 6]]]]

print(nums[0])
print(nums[0][2])
print(nums[0][2][2])

print(nums[0][0])
print(nums[0][2][1])
print(nums[0][2][2][0])
```

In the example, the `[5, 6]` list is nested into `[3, 4, ...]` list, the `[3, 4, [4, 6]]` is nested into the `[1, 2, ...]`  
list which is finally an element of the nums list.  

```python
print(nums[0])
print(nums[0][2])
print(nums[0][2][2])
```

These three lines print the nested lists to the console.

```python
print(nums[0][0])
print(nums[0][2][1])
print(nums[0][2][2][0])
```

Here three elements are accessed. Additional square brackets `[]` are needed when referring to inner lists.

```python
$ ./nested2.py
[1, 2, [3, 4, [5, 6]]]
[3, 4, [5, 6]]
[5, 6]
1
4
5
```

## Sort list

In this section we sort list elements. Python has a built-in list method sort and sorted function  
for doing sorting. 

```python
#!/usr/bin/python

# sorting.py

n = [3, 4, 7, 1, 2, 8, 9, 5, 6]
print(n)

n.sort()
print(n)

n.sort(reverse=True)
print(n)
```

In the code example, we have a list of unsorted integers. We sort the elements using the sort method.  
The method sorts the elements in-place; the original list is modified.  

```python
n.sort()
```

The `sort` method sorts the elements in ascending order.

```python
n.sort(reverse=True)
```

With the reverse parameter set to `True`, the list is sorted in a descending order.  

```python
$ ./sorting.py
[3, 4, 7, 1, 2, 8, 9, 5, 6]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

In the output we can see the original list, the sorted list in ascending and descending orders.  

If we do not want to change the original list, we can use the sorted function. This function  
creates a new sorted list.  

```python
#!/usr/bin/python

# sorting2.py

n = [3, 4, 1, 7, 2, 5, 8, 6]

print(n)
print(sorted(n))
print(n)
```

In the example, we use the sorted function to sort the elements of a list.

```
$ ./sorting2.py
[3, 4, 1, 7, 2, 5, 8, 6]
[1, 2, 3, 4, 5, 6, 7, 8]
[3, 4, 1, 7, 2, 5, 8, 6]
```

From the output of the script we can see that the original list is not modified.  

The sort method has an optional key parameter. The parameter specifies a function  
to be called on each list element prior to making comparisons.  

```python
#!/usr/bin/python

# sorting3.py

words = ["big", "Blue", "seven", "glass",
         "Green", "after", "Anctartica"]

words.sort()
print(words)

words.sort(key=str.lower)
print(words)
```

The example produces a case-sensitive and case-insensitive string comparison.

```python
words.sort(key=str.lower)
```

To create a case-insensitive comparison, we add the str.lower function to the key parameter.

```
$ ./sorting3.py
['Anctartica', 'Blue', 'Green', 'after', 'big', 'glass', 'seven']
['after', 'Anctartica', 'big', 'Blue', 'glass', 'Green', 'seven']
```

We need to do additional work if we want to sort Unicode strings.

```python
#!/usr/bin/python

import locale
from functools import cmp_to_key

w = [u'zem', u'štebot', u'rum', u'železo', u'prameň', u"sob"]
locale.setlocale(locale.LC_COLLATE, ('sk_SK', 'UTF8'))

w.sort(key=cmp_to_key(locale.strcoll))

for e in w:
    print(e)
```

We have a list of six unicode strings. We change the locale settings to sort the  
strings according to current language option.  

```python
import locale
from functools import cmp_to_key
```

We import the locale module and the `cmp_to_key` conversion function.  

```python
w = [u'zem', u'štebot', u'rum', u'železo', u'prameň', u"sob"]
```

This is a list of six strings. The strings are in Slovak language and have some  
diacritical marks. They play role in sorting the characters correctly.  

```python
locale.setlocale(locale.LC_COLLATE, ('sk_SK', 'UTF8'))
```

We set the locale settings for the Slovak language.

```python
w.sort(key=cmp_to_key(locale.strcoll))
```

We sort the list. The `locale.strcoll` compares two strings according to the current `LC_COLLATE` 
setting. The `cmp_to_key` function transform an old-style comparison function to a key-function.

```python
for e in w:
    print(e)
```

We print the sorted words to the console.

```python
$ ./sorting_locale.py
prameň
rum
sob
štebot
zem
železo
```

The elements were correctly sorted. The specifics of the Slovak alphabet were taken into account.

## Reverse list elements

We can reverse elements in a list in a few ways in Python. Reversing elements should not be  
confused with sorting in a reverse way.

```python
#!/usr/bin/python

# reversing.py

a1 = ["bear", "lion", "tiger", "eagle"]
a2 = ["bear", "lion", "tiger", "eagle"]
a3 = ["bear", "lion", "tiger", "eagle"]

a1.reverse()
print(a1)

it = reversed(a2)
r = list()

for e in it:
    r.append(e)

print(r)

print(a3[::-1])
```

In the example, we have three identical string lists. We reverse the elements in three different ways.  

```python
a1.reverse()
```

The first way is to use the reverse method.

```python
it = reversed(a2)
r = list()

for e in it:
    r.append(e)
```

The `reversed` function returns a reverse iterator. We use the iterator in a for loop and create  
a new reversed list.

```python
print(a3[::-1])
```

The third way is to reverse the list using the slice syntax, where the step parameter is set to -1.

```python
$ ./reversing.py
['eagle', 'tiger', 'lion', 'bear']
['eagle', 'tiger', 'lion', 'bear']
['eagle', 'tiger', 'lion', 'bear']
```

All the three lists were reversed OK.

# List comprehension

A list comprehension is a syntactic construct which creates a list based on existing list. The syntax was  
influenced by mathematical notation of sets. The Python syntax was inspired by the Haskell programming language. 

```
L = [expression for variable in sequence [if condition]]
```

The above pseudo code shows the syntax of a list comprehension. A list comprehension creates a new list. It is  
based on an existing list. A for loop goes through the sequence. For each loop an expression is evaluated if the  
condition is met. If the value is computed it is appended to the new list. The condition is optional. 

List comprehensions provide a more concise way to create lists in situations where map and filter and/or  
nested loops could be used.  

```python
#!/usr/bin/python

# list_comprehension.py

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [e for e in a if e % 2]
print(b)
```

In the example we have defined a list of numbers. With the help of the list comprehension, we create  
a new list of numbers that cannot be divided by 2 without a remainder. 

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [e for e in a if e % 2]
```

Here we have the list comprehension. In the `for e in a` loop each element of a list is taken. Then `a if e % 2`  
condition is tested. If the condition is met, an expression is evaluated. In our case the expression  
is a pure `e` which takes the element as it is. Finally, the element is appended to the list.

```
$ ./list_comprehension.py
[1, 3, 5, 7, 9]
```

The numbers in a list cannot be divided by 2, without a remainder.

In the second example we compare a list comprehension to a traditional for loop. 

```python
#!/usr/bin/python

# list_comprehension2.py

lang = "Python"

a = []

for e in lang:
    a.append(ord(e))

b = [ord(e) for e in lang]

print(a)
print(b)
```

In the example we have a string. We want to create a list of the ASCII integer codes of the letters of the string.

```python
a = []

for e in lang:
    a.append(ord(e))
```

We create such a list with the for loop.

```python
b = [ord(e) for e in lang]
```

Here the same is produced using a list comprehension. Note that the if condition was omitted.  
It is optional.

```
$ ./list_comprehension2.py
[80, 121, 116, 104, 111, 110]
[80, 121, 116, 104, 111, 110]
```

Check Python list comprehensions for more details.

## The map and filter functions

The `map` and `filter` functions are mass functions that work on all list items. They are part of  
the functional programming built into the Python language.

Today, it is recommended to use list comprehensions instead of these functions where possible.  

```python
#!/usr/bin/python

# map_fun.py

def to_upper(s):

    return s.upper()

words = ["stone", "cloud", "dream", "sky"]

words2 = list(map(to_upper, words))
print(words2)
```

The `map` function applies a particular function to every element of a list.

```python
def to_upper(s):

    return s.upper()
```

This is the definition of the function that will be applied to every list element.  
It calls the upper string method on a given string.

```python
words = ["stone", "cloud", "dream", "sky"]
words2 = map(to_upper, words)
print(words2)
```

The map function applies the to_upper function to every string element of the words list.  
A new list is formed and returned back. We print it to the console.  

```
$ ./map_fun.py
['STONE', 'CLOUD', 'DREAM', 'SKY']
```

Every item of the list is in capital letters.

The `filter` function constructs a list from those elements of the list for which a function returns true.

```python
#!/usr/bin/python

# filter_fun.py

def positive(x):
    return x > 0

n = [-2, 0, 1, 2, -3, 4, 4, -1]

print(list(filter(positive, n)))
```

An example demonstrating the `filter` function. It creates a new list having only positive values.  
It filters out all negative values and 0.

```python
def positive(x):
    return x > 0
```

This is the definition of the function used by the `filter` function. It returns `True` or `False`. 
Functions that return a boolean value are called *predicates*.

```
$ ./filter_fun.py
[1, 2, 4, 4]
```
