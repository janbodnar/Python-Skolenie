# Indexing and Slicing

Many Python values hold several items in a fixed order: the characters of  
a string, the items of a list, the values of a tuple. Such values are  
called **sequences**. Every item in a sequence has a position, and square  
brackets let you work with items by their position:

- `fruits[0]` gets one item; this is called **indexing**,
- `fruits[1:3]` gets a part of the sequence; this is called **slicing**.

The Python Language Reference calls the first form a **subscription**, and  
error messages use that word too, as in "object is not subscriptable".

This chapter covers these topics:

- sequences and positions,
- indexing with positive and negative indexes,
- slicing, with and without a step,
- changing lists with indexes and slices,
- nested indexing,
- indexes in `for` loops,
- dictionaries and sets, which do not use positions.

The chapter ends with common mistakes and a hands-on example that  
processes weather data with indexes and slices.

## Sequences

Python has four common sequence types: strings, lists, tuples, and ranges.  
They hold different kinds of data, but you read their items in the same  
way:

```python
# sequences.py

word = "Python"
fruits = ["apple", "banana", "cherry"]
point = (3, 7)
numbers = range(10, 20)

print(word[0], fruits[0], point[0], numbers[0])
print(len(word), len(fruits), len(point), len(numbers))
```

```text
$ python sequences.py
P apple 3 10
6 3 2 10
```

`[0]` returns the first item of each sequence, and `len()` returns the  
number of items. Everything in this chapter works for all four types,  
except changing items, which only lists allow.

## Indexing

### Positive Indexes

The position of an item is its **index**. Counting starts at 0, so the  
first item has the index 0, the second item the index 1, and the last  
item the index `len(sequence) - 1`:

```python
# indexing.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]

print(names[0])
print(names[1])
print(names[4])
print(names[len(names) - 1])
```

```text
$ python indexing.py
Anna
Ben
Eva
Eva
```

The list has five items, so the indexes go from 0 to 4. Counting from zero  
feels strange at first. It helps to think of the index as the distance  
from the start: the first item is zero steps away from it.

### Negative Indexes

A negative index counts from the end. `-1` is the last item, `-2` the one  
before it, and so on:

```text
 "Anna"  "Ben"  "Cleo"  "Dan"  "Eva"
    0      1      2       3      4
   -5     -4     -3      -2     -1
```

```python
# negative.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]

print(names[-1])
print(names[-2])
print(names[-5])
```

```text
$ python negative.py
Eva
Dan
Anna
```

`names[-1]` is a short and clear way to write `names[len(names) - 1]`.  
Use it whenever you need the last item.

### Index Out of Range

An index must point to an existing item. A larger index is an error:

```python
# index_error.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]
print(names[5])
```

```text
$ python index_error.py
Traceback (most recent call last):
  File ".../index_error.py", line 4, in <module>
    print(names[5])
          ~~~~~^^^
IndexError: list index out of range
```

The list has five items, so the last valid index is 4. Strings and tuples  
raise the same error, with the message `string index out of range` or  
`tuple index out of range`. The smallest valid negative index is `-5`,  
and `names[-6]` fails as well.

## Slicing

### Start and Stop

A **slice** returns a part of a sequence. You write it as  
`sequence[start:stop]`. The slice begins at the index `start` and ends  
*before* the index `stop`:

```python
# slicing.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]

print(names[1:3])
print(names[0:2])
print(names[2:5])
```

```text
$ python slicing.py
['Ben', 'Cleo']
['Anna', 'Ben']
['Cleo', 'Dan', 'Eva']
```

The item at `stop` is not included, so `names[1:3]` returns the items at  
the indexes 1 and 2. A useful rule: the slice `[start:stop]` has  
`stop - start` items.

It helps to picture the indexes as positions *between* the items, like  
the marks on a ruler. A slice returns everything between two marks:

```text
 +------+-----+------+-----+-----+
 | Anna | Ben | Cleo | Dan | Eva |
 +------+-----+------+-----+-----+
 0      1     2      3     4     5
-5     -4    -3     -2    -1
```

`names[1:3]` takes everything between mark 1 and mark 3: Ben and Cleo.

### Leaving Out Start or Stop

If you leave out `start`, the slice begins at the start of the sequence.  
If you leave out `stop`, it goes to the end:

```python
# slice_ends.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]

print(names[:2])
print(names[2:])
print(names[-2:])
print(names[:-1])
print(names[:])
```

```text
$ python slice_ends.py
['Anna', 'Ben']
['Cleo', 'Dan', 'Eva']
['Dan', 'Eva']
['Anna', 'Ben', 'Cleo', 'Dan']
['Anna', 'Ben', 'Cleo', 'Dan', 'Eva']
```

These forms are the ones you will use most often:

| Slice | Meaning |
| --- | --- |
| `names[:n]` | The first `n` items |
| `names[n:]` | Everything except the first `n` items |
| `names[-n:]` | The last `n` items |
| `names[:-n]` | Everything except the last `n` items |
| `names[:]` | All items, as a new copy |

`names[:2]` and `names[2:]` split the list into two parts with nothing  
missing and nothing repeated. This works for any number in place of `2`.

### Slices Never Fail

Unlike an index, a slice does not raise an error when it goes past the  
end. It returns as many items as exist, or an empty sequence:

```python
# slice_range.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]

print(names[3:100])
print(names[10:])
print(names[3:1])
```

```text
$ python slice_range.py
['Dan', 'Eva']
[]
[]
```

`names[3:1]` is empty because the slice would have to go backwards. This  
behaviour is convenient: `names[:3]` safely returns *up to* three items,  
even from a shorter list.

### Slicing with a Step

A third number, the **step**, sets the distance between the items. The  
full form is `sequence[start:stop:step]`:

```python
# step.py

numbers = [0, 10, 20, 30, 40, 50, 60]

print(numbers[::2])
print(numbers[1::2])
print(numbers[1:6:2])
print(numbers[::3])
```

```text
$ python step.py
[0, 20, 40, 60]
[10, 30, 50]
[10, 30, 50]
[0, 30, 60]
```

`[::2]` takes every second item, starting with the first. `[1::2]` starts  
with the second item instead. The step is `1` when you leave it out.

A negative step goes backwards. The most common case is `[::-1]`, which  
reverses a sequence:

```python
# reverse.py

word = "Python"
names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]

print(word[::-1])
print(names[::-1])
print(names[3:0:-1])
```

```text
$ python reverse.py
nohtyP
['Eva', 'Dan', 'Cleo', 'Ben', 'Anna']
['Dan', 'Cleo', 'Ben']
```

With a negative step, `start` must be *larger* than `stop`.  
`names[3:0:-1]` starts at index 3 and goes back to index 1; index 0 is  
the `stop` and is not included. Slices with a negative step and explicit  
bounds are hard to read, so use them sparingly.

### A Slice Is a New Object

A slice has the same type as the sequence: a slice of a string is a  
string, a slice of a list is a new list, and a slice of a tuple is a  
tuple. For lists, this means a slice is a copy:

```python
# slice_copy.py

names = ["Anna", "Ben", "Cleo"]
first_two = names[:2]

first_two.append("Zoe")

print(first_two)
print(names)
print(type("Python"[1:4]), "Python"[1:4])
```

```text
$ python slice_copy.py
['Anna', 'Ben', 'Zoe']
['Anna', 'Ben', 'Cleo']
<class 'str'> yth
```

Changing `first_two` did not change `names`. This is why `names[:]`  
is a common way to copy a list; `names.copy()` does the same and is more  
explicit.

## Changing Lists with Indexes and Slices

### Assigning to an Index

Lists are mutable, so you can replace an item by assigning to its index:

```python
# assign_index.py

names = ["Anna", "Ben", "Cleo"]

names[0] = "Alice"
names[-1] = "Carol"
print(names)
```

```text
$ python assign_index.py
['Alice', 'Ben', 'Carol']
```

The index must already exist; `names[3] = "Dan"` raises an `IndexError`.  
To add an item, use `append()` or `insert()`.

Strings and tuples are immutable, so assigning to an index of a string or  
a tuple raises a `TypeError`, for example `'str' object does not support  
item assignment`.

### Deleting with `del`

The `del` statement removes an item, or a whole slice, from a list:

```python
# delete.py

numbers = [0, 10, 20, 30, 40, 50]

del numbers[0]
print(numbers)

del numbers[1:3]
print(numbers)
```

```text
$ python delete.py
[10, 20, 30, 40, 50]
[10, 40, 50]
```

After the first `del`, the items move one place to the left, so their  
indexes change. Keep this in mind when you delete several items one after  
another.

### Assigning to a Slice

You can also assign a list to a slice. The items in the slice are replaced  
by the new items, and the list grows or shrinks as needed:

```python
# assign_slice.py

numbers = [1, 2, 3, 4, 5]

numbers[1:3] = [20, 30]
print(numbers)

numbers[1:3] = [7, 7, 7, 7]
print(numbers)

numbers[1:5] = []
print(numbers)
```

```text
$ python assign_slice.py
[1, 20, 30, 4, 5]
[1, 7, 7, 7, 7, 4, 5]
[1, 4, 5]
```

The first assignment replaces two items with two others. The second  
replaces two items with four, so the list becomes longer. The third  
replaces four items with nothing, which deletes them.

## Nested Indexing

The items of a list can themselves be lists, tuples, or strings. To reach  
an item inside an item, write several pairs of brackets one after  
another. Python applies them from left to right:

```python
# nested.py

seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"],
]

print(seats[1])
print(seats[1][2])
print(seats[-1][0])

names = ["Anna", "Ben", "Cleo"]
print(names[2][0])
```

```text
$ python nested.py
['B1', 'B2', 'B3']
B3
C1
C
```

`seats` is a list of rows, and each row is a list of seats. `seats[1]` is  
the second row, and `seats[1][2]` is the third seat in that row. In the  
same way, `names[2]` is the string `"Cleo"`, and `names[2][0]` is its  
first letter.

Nested indexing also works across types. When a dictionary holds lists,  
`grades["Alice"][0]` is the first score of Alice.

## Indexes in Loops

### Looping over Items

To process all items of a sequence, loop over the items directly. You do  
not need any indexes:

```python
# loop_items.py

names = ["Anna", "Ben", "Cleo"]

for name in names:
    print(name)
```

```text
$ python loop_items.py
Anna
Ben
Cleo
```

### Getting the Index with `enumerate()`

When you need the position as well, use the built-in `enumerate()`  
function. It gives you the index and the item together:

```python
# enumerate_names.py

names = ["Anna", "Ben", "Cleo"]

for index, name in enumerate(names):
    print(index, name)

for number, name in enumerate(names, start=1):
    print(f"{number}. {name}")
```

```text
$ python enumerate_names.py
0 Anna
1 Ben
2 Cleo
1. Anna
2. Ben
3. Cleo
```

`start=1` makes the numbering begin at 1, which is what people expect in  
a numbered list. You may see code that loops with  
`for i in range(len(names))` and then reads `names[i]`. It works, but  
`enumerate()` is shorter and harder to get wrong.

### Finding the Index of a Value

The `index()` method works in the opposite direction: it returns the  
index of a value. It raises a `ValueError` when the value is missing, so  
check with `in` first if you are not sure:

```python
# find_index.py

names = ["Anna", "Ben", "Cleo", "Ben"]

print(names.index("Ben"))

if "Zoe" in names:
    print(names.index("Zoe"))
else:
    print("Zoe is not in the list")
```

```text
$ python find_index.py
1
Zoe is not in the list
```

`index()` returns the first occurrence, so the second `"Ben"` at index 3  
is not found.

## Dictionaries and Sets

Dictionaries also use square brackets, but with a **key** instead of a  
position. Sets have no positions and no keys, so they do not support  
square brackets at all:

```python
# keys.py

ages = {"Anna": 30, "Ben": 25}
print(ages["Ben"])

colors = {"red", "green", "blue"}
print(colors[0])
```

```text
$ python keys.py
25
Traceback (most recent call last):
  File ".../keys.py", line 7, in <module>
    print(colors[0])
          ~~~~~~^^^
TypeError: 'set' object is not subscriptable
```

`ages["Ben"]` looks up the key `"Ben"`. A dictionary has no "first item"  
in the sense of an index: `ages[0]` looks for the key `0` and raises a  
`KeyError`, and a dictionary cannot be sliced. For a set, use `in` to  
check whether a value is present, or convert it to a sorted list first:  
`sorted(colors)[0]`.

| Type | How you get an item | Example |
| --- | --- | --- |
| `str`, `list`, `tuple`, `range` | by position | `names[0]` |
| `dict` | by key | `ages["Ben"]` |
| `set` | no access to single items; check with `in` | `"red" in colors` |

## Common Mistakes

### Using the Length as an Index

The length of a sequence is one more than its last index:

```python
# length_index.py

names = ["Anna", "Ben", "Cleo"]
last = names[len(names)]
```

```text
$ python length_index.py
Traceback (most recent call last):
  File ".../length_index.py", line 4, in <module>
    last = names[len(names)]
           ~~~~~^^^^^^^^^^^^
IndexError: list index out of range
```

`len(names)` is 3, but the indexes are 0, 1, and 2. Use `names[-1]` to  
get the last item. This kind of mistake, being one step off, is so common  
that it has a name: an **off-by-one error**.

### Using a Float as an Index

An index must be an integer. The `/` operator always returns a float, even  
for an exact division, so it cannot be used to compute an index:

```python
# middle.py

names = ["Anna", "Ben", "Cleo", "Dan", "Eva"]
middle = len(names) / 2
print(names[middle])
```

```text
$ python middle.py
Traceback (most recent call last):
  File ".../middle.py", line 5, in <module>
    print(names[middle])
          ~~~~~^^^^^^^^
TypeError: list indices must be integers or slices, not float
```

Use floor division `//`, which returns an integer:  
`names[len(names) // 2]` is `"Cleo"`.

### Expecting the Stop Item in a Slice

The item at the `stop` index is not part of the slice. To get the items at  
the indexes 1, 2, and 3, write `names[1:4]`, not `names[1:3]`. Remember  
the rule: `[start:stop]` has `stop - start` items.

### Copying a Nested List with a Slice

A slice copies only the outer list. The inner lists are not copied; both  
lists refer to the same inner lists:

```python
# shallow_copy.py

board = [[0, 0], [0, 0]]
board_copy = board[:]

board_copy[0][0] = 1
print(board)
```

```text
$ python shallow_copy.py
[[1, 0], [0, 0]]
```

Changing `board_copy[0][0]` also changed `board`, because `board_copy[0]`  
and `board[0]` are the same list. This is called a **shallow copy**. To copy  
the inner lists as well, use `copy.deepcopy()` from the `copy` module.

## Hands-On: A Week of Weather

This program reads a week of temperature readings stored as text. It uses  
string slicing to take each line apart, negative indexes and slices to  
select days, nested indexing to read values from a list of tuples, and  
`enumerate()` to find the warmest day.

```python
# weather.py

readings = [
    "2026-11-16 6.5",
    "2026-11-17 4.0",
    "2026-11-18 7.5",
    "2026-11-19 3.0",
    "2026-11-20 5.5",
    "2026-11-21 8.0",
    "2026-11-22 2.5",
]

days = []
for line in readings:
    date = line[:10]
    temperature = float(line[11:])
    days.append((date, temperature))

print("Year:", days[0][0][:4])
print("From", days[0][0], "to", days[-1][0])

last_three = days[-3:]
total = 0
for day in last_three:
    total += day[1]
print(f"Average of the last 3 days: {total / len(last_three):.1f}")

warmest = 0
for index, day in enumerate(days):
    if day[1] > days[warmest][1]:
        warmest = index
print("Warmest day:", days[warmest][0][5:], days[warmest][1])

print("Weekend:")
for day in days[-2:]:
    print(" ", day[0][5:], day[1])
```

```text
$ python weather.py
Year: 2026
From 2026-11-16 to 2026-11-22
Average of the last 3 days: 5.3
Warmest day: 11-21 8.0
Weekend:
  11-21 8.0
  11-22 2.5
```

- `line[:10]` takes the first ten characters, the date, and `line[11:]`  
  takes everything after the space, the temperature.
- `days` is a list of tuples, so `days[0][0]` is the date of the first  
  day, and `days[0][0][:4]` is the first four characters of that date,  
  the year.
- `days[-1]` is the last day, `days[-3:]` the last three days, and  
  `days[-2:]` the weekend.
- `warmest` stores the *index* of the warmest day found so far.  
  `enumerate()` supplies the index of each day for the comparison.
- `[5:]` cuts the year off a date, leaving the month and the day.

## Summary

| Syntax | Meaning |
| --- | --- |
| `s[i]` | The item at index `i`; the first index is 0 |
| `s[-1]` | The last item; negative indexes count from the end |
| `s[start:stop]` | Items from `start` up to, but not including, `stop` |
| `s[:n]`, `s[-n:]` | The first `n` items, the last `n` items |
| `s[::step]` | Every `step`-th item |
| `s[::-1]` | The sequence reversed |
| `s[:]` | A shallow copy of the sequence |
| `lst[i] = x` | Replace an item of a list |
| `lst[a:b] = items` | Replace a slice of a list; the length may change |
| `del lst[i]`, `del lst[a:b]` | Remove an item or a slice from a list |
| `s[i][j]` | Nested indexing: item `j` of item `i` |
| `enumerate(s)` | Loop over indexes and items together |
| `IndexError` | An index that points past the end of a sequence |

Indexes point to single items and must exist; slices select ranges and  
never fail. Dictionaries use keys instead of positions, and sets cannot be  
indexed at all.

## References

- [The Python Tutorial: Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [The Python Tutorial: Text](https://docs.python.org/3/tutorial/introduction.html#text)
- [Built-in Types: Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Built-in Types: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
- [The Python Language Reference: Subscriptions and Slicings](https://docs.python.org/3/reference/expressions.html#subscriptions-and-slicings)
- [Built-in Functions: `enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)
- [`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)
