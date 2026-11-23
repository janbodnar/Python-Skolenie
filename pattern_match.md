# Pattern Matching

*Pattern matching* compares a value against a series of **patterns** and  
runs the block of the first pattern that matches. Python 3.10 introduced  
it as **structural pattern matching**, using the `match` and `case`  
keywords. The word *structural* refers to the fact that a pattern can  
describe the structure of data, not just its value.

A pattern can look inside a list, a dictionary, or an object, bind parts  
of the value to names, and add extra conditions. That makes pattern  
matching more expressive than a chain of `if/elif` tests or a classic  
`switch` statement.

The value after `match` is the **subject**, and each pattern after `case`  
together with its indented block forms an **arm**. In an `if/elif` chain  
the blocks are usually called *branches*; pattern matching uses the word  
*arm* instead.

Unlike a C-style `switch`, Python does not fall through. The first arm  
that matches wins, the remaining arms are skipped, and no `break` is  
needed. If no arm matches, nothing happens and execution continues after  
the `match` statement.

The chapter starts with the simplest patterns and builds up to nested  
ones:

- literal patterns and alternatives,
- the wildcard and capture patterns,
- guards,
- sequences, mappings, and class instances,
- enum members,
- `as` patterns and nested patterns.

## Matching Literal Values

A **literal pattern** compares the subject with a value written directly  
in the pattern. The first example greets a list of languages.

```python
# literals.py

langs = ["russian", "slovak", "german",
         "swedish", "hungarian", "french", "spanish"]

print("say hello")

for lang in langs:
    match lang:
        case "russian":
            print("привет")
        case "slovak":
            print("ahoj")
        case "german":
            print("hallo")
        case "swedish":
            print("Hallå")
        case "hungarian":
            print("szia")
        case "french":
            print("salut")
        case "spanish":
            print("hola")
```

The `match` keyword is followed by the subject and a colon. Each arm  
starts with `case`, followed by a pattern and a colon:

```python
match lang:
    case "russian":
        print("привет")
```

If the pattern matches the subject, the indented block runs. The subject  
is evaluated once, before the first arm is tested.

```text
$ python literals.py
say hello
привет
ahoj
hallo
Hallå
szia
salut
hola
```

String comparison is exact and case-sensitive, so `"Russian"` would not  
match `"russian"`. A value that matches no arm is silently ignored; we  
return to that behaviour in Common Mistakes.

## Alternatives in One Arm

The vertical bar `|` combines patterns into an **OR pattern**. The arm  
runs when any of the alternatives matches. Here, all passing grades share  
one block.

```python
# grades.py

grades = ["A", "B", "C", "D", "E", "F", "FX"]

for grade in grades:
    match grade:
        case "A" | "B" | "C" | "D" | "E" | "F":
            print("passed")
        case "FX":
            print("failed")
```

The bar belongs to the pattern syntax; it is not the bitwise OR  
operator. An OR pattern is useful when several values should produce the  
same result, because the repeated code lives in a single arm.

```text
$ python grades.py
passed
passed
passed
passed
passed
passed
failed
```

## The Wildcard Pattern

The underscore `_` is the **wildcard pattern**. It matches any value but  
does not bind that value to a name. Because it always matches, it must  
come last; otherwise the arms below it could never run.

The next example computes factorials with `match/case`.

```python
# factorial.py

def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)

for i in range(13):
    print(i, factorial(i))
```

For `0` and `1` the function returns `1`. For every other value, the  
wildcard matches and the function calls itself with a smaller argument.

```text
$ python factorial.py
0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800
11 39916800
12 479001600
```

The function assumes that `n` is a non-negative integer. A negative  
argument would recurse until the interpreter raises `RecursionError`, so  
real code should validate the input before calling `factorial`.

## Capture Patterns

A bare name in a pattern is a **capture pattern**. It matches any value  
and binds that value to the name.

```python
# capture.py

values = [0, 7, -2]

for value in values:
    match value:
        case 0:
            print("zero")
        case other:
            print(f"not zero: {other}")
```

In `case 0:` the zero is a literal pattern, but in `case other:` the word  
`other` is a new variable. A capture pattern always succeeds, so it must  
be last, just like the wildcard. The difference is that a capture also  
gives you the matched value.

```text
$ python capture.py
zero
not zero: 7
not zero: -2
```

Captures are how patterns extract data from larger structures. They are  
also a common source of bugs: a name that looks like a constant captures  
instead of comparing, as we will see in Common Mistakes.

## Guards

A **guard** is an `if` condition attached to an arm. The arm is chosen  
only when the pattern matches **and** the guard evaluates to `True`.

```python
# guards.py

numbers = [-7, 0, 4]

for number in numbers:
    match number:
        case n if n < 0:
            print(f"{n}: negative value")
        case n if n == 0:
            print(f"{n}: zero")
        case n if n > 0:
            print(f"{n}: positive value")
```

First the capture pattern binds `n`, then the guard is evaluated. The  
guard can use the captured names, outer variables, or both.

```text
$ python guards.py
-7: negative value
0: zero
4: positive value
```

If no guard is true and there is no wildcard arm, the whole `match`  
statement does nothing. A final `case _:` is a good habit when every  
value needs a result.

## Sequence Patterns

**Sequence patterns** match lists, tuples, and other sequences such as  
`range`. They do not match `str` or `bytes`, even though those types are  
sequences; text is matched with literal or class patterns instead.

```python
# sequences.py

records = [
    ("Alice", "Engineering", 85000),
    ("Bob", "Sales", 62000),
    ("Charlie", "Engineering", 91000),
    ("Diana", "HR", 55000),
]

for record in records:
    match record:
        case (name, "Engineering", salary):
            print(f"{name} works in Engineering and earns ${salary}")
        case (name, dept, salary) if salary < 60000:
            print(f"{name} from {dept} earns less than $60k")
        case (name, dept, _):
            print(f"{name} works in {dept}")
```

A sequence pattern without a star matches exactly as many items as it  
contains. The first arm requires three items and the second item to be  
`"Engineering"`. The second arm uses a guard to select lower salaries,  
and the third arm ignores the salary with `_`.

Square brackets and parentheses are interchangeable here: `[a, b]` and  
`(a, b)` both match any two-item sequence.

```text
$ python sequences.py
Alice works in Engineering and earns $85000
Bob works in Sales
Charlie works in Engineering and earns $91000
Diana from HR earns less than $60k
```

Arms are tested from top to bottom, so specific patterns must come before  
general ones. Bob earns 62000, so the guard in the second arm is false and  
he matches the third arm. Diana earns 55000, so she matches the second arm  
before the third can run.

## Variable-Length Sequence Patterns

A star pattern such as `*rest` matches any number of items. It binds a  
list, which may be empty. A sequence pattern may contain at most one  
star.

```python
# star_pattern.py

def process_first_two(items):
    match items:
        case [first, second, *rest]:
            print(f"First: {first}, Second: {second}, Rest: {rest}")
        case [first, *rest]:
            print(f"Only first: {first}, Rest: {rest}")
        case _:
            print("Empty list")

process_first_two([10, 20, 30, 40])
process_first_two([5])
process_first_two([])
```

The first arm needs at least two items, the second needs at least one,  
and the wildcard handles the empty list.

```text
$ python star_pattern.py
First: 10, Second: 20, Rest: [30, 40]
Only first: 5, Rest: []
Empty list
```

The star can appear in any position. Here `middle` collects everything  
between the first and the last item, and it may be empty:

```python
for items in [[1, 2, 3, 4], [1, 2]]:
    match items:
        case [first, *middle, last]:
            print(first, middle, last)
```

```text
1 [2, 3] 4
1 [] 2
```

## Mapping Patterns

**Mapping patterns** match dictionaries by keys. Only the keys listed in  
the pattern must be present; extra keys are allowed and ignored. Key  
order does not matter.

```python
# maps.py

users = [
    {"name": "Paul", "cols": ["red", "blue", "salmon"]},
    {"name": "Martin", "cols": ["blue"]},
    {"name": "Lucia", "cols": ["pink", "brown"]},
    {"name": "Jan", "cols": ["blue", "green"]},
]

for user in users:
    match user:
        case {"name": name, "cols": cols}:
            print(f"favourite colours of {name}:")
            for col in cols:
                print(col)
```

The pattern `{"name": name, "cols": cols}` matches any dictionary that  
has at least the keys `"name"` and `"cols"`. It binds the corresponding  
values to the variables `name` and `cols`.

```text
$ python maps.py
favourite colours of Paul:
red
blue
salmon
favourite colours of Martin:
blue
favourite colours of Lucia:
pink
brown
favourite colours of Jan:
blue
green
```

> **Note**: A mapping pattern is partial by design. The pattern  
> `{"name": name}` also matches `{"name": "Paul", "age": 30}`, because  
> extra keys are not an error.

To see or check the remaining keys, add `**rest` at the end of the  
pattern:

```python
# maps_rest.py

user = {"name": "Paul", "cols": ["red", "blue"]}

match user:
    case {"name": name, "cols": cols, **rest} if not rest:
        print(f"{name} has exactly two keys")
    case {"name": name, **rest}:
        print(f"{name} has extra keys: {list(rest)}")
```

`rest` receives a dictionary of the other items. Adding `**rest` does not  
reject extra keys; to require exactly the listed keys, combine it with  
the guard `if not rest`, as the first arm does.

```text
$ python maps_rest.py
Paul has exactly two keys
```

## Class Patterns

**Class patterns** test whether the subject is an instance of a class (or  
a subclass) and then match its attributes. They do not create a new  
object; they inspect an existing one.

```python
# objects.py

from dataclasses import dataclass


@dataclass
class Cat:
    name: str


@dataclass
class Dog:
    name: str


@dataclass
class Person:
    name: str


items = [Cat("Missy"), Dog("Jasper"), Dog("Ace"),
         Person("Peter"), "Jupiter"]

for item in items:
    match item:
        case Cat(name) | Dog(name):
            print(f"{name} is a pet")
        case Person(name):
            print(f"{name} is a human")
        case _:
            print("unknown")
```

`case Cat(name)` succeeds for a `Cat` and binds its `name` attribute. The  
OR pattern combines `Cat(name)` and `Dog(name)`; both alternatives bind  
the same name, which is required for an OR pattern.

```text
$ python objects.py
Missy is a pet
Jasper is a pet
Ace is a pet
Peter is a human
unknown
```

The wildcard catches the string `"Jupiter"`, which is not an instance of  
any of the three classes. For classes that inherit from one another,  
list the most specific pattern first.

## Positional Patterns

`Cat(name)` and `Point(0, 0)` are **positional patterns**. The values in  
the pattern are matched against attributes in a fixed order, and that  
order comes from the class attribute `__match_args__`.

```python
# positional_match.py

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


print(Point.__match_args__)


def describe(point):
    match point:
        case Point(0, 0):
            print("Origin")
        case Point(0, y):
            print(f"On Y-axis at y={y}")
        case Point(x, 0):
            print(f"On X-axis at x={x}")
        case Point(x, y):
            print(f"Point at ({x}, {y})")


describe(Point(0, 0))
describe(Point(0, 5))
describe(Point(3, 0))
describe(Point(2, 7))
```

`@dataclass` generates `__match_args__` from the fields that take part  
in `__init__`, in their order, so we do not have to write the tuple. For  
a class that is not a data class, set it yourself, for example  
`__match_args__ = ("x", "y")`.

```text
$ python positional_match.py
('x', 'y')
Origin
On Y-axis at y=5
On X-axis at x=3
Point at (2, 7)
```

Keyword patterns name the attributes and do not depend on  
`__match_args__`: `case Point(x=0, y=y)` is equivalent to  
`case Point(0, y)` for this class. Positional elements must come before  
keyword elements in one pattern.

## Matching Enums

Enum members are named constants, and they are a natural fit for pattern  
matching.

```python
# enums.py

from enum import Enum


Day = Enum("Day", "Monday Tuesday Wednesday Thursday Friday Saturday Sunday")

for day in Day:
    match day:
        case Day.Saturday | Day.Sunday:
            print(f"{day.name} is a weekend")
        case _:
            print(f"{day.name} is a weekday")
```

`Day.Saturday` is a **value pattern**: the dot makes Python look up the  
existing member instead of creating a capture variable. A bare  
`Saturday` in a pattern would capture any value. This is the same reason  
that `case german` did not compare with the variable `german` in Common  
Mistakes.

```text
$ python enums.py
Monday is a weekday
Tuesday is a weekday
Wednesday is a weekday
Thursday is a weekday
Friday is a weekday
Saturday is a weekend
Sunday is a weekend
```

## The `as` Pattern

The `as` keyword binds the whole subject while a pattern matches its  
parts. This is useful when you need both the pieces and the original  
value, for example for logging.

```python
# as_pattern.py


def inspect_command(cmd):
    match cmd.split():
        case ["quit"]:
            print("Exiting...")
        case ["load", filename] as whole:
            print(f"Loading file {filename!r} (full command: {whole})")
        case _:
            print("Unknown command")


inspect_command("load data.txt")
```

`whole` is the list returned by `split()`, while `filename` is its second  
item. The `as` clause applies to the pattern on its left, so it captures  
the entire two-item list.

```text
$ python as_pattern.py
Loading file 'data.txt' (full command: ['load', 'data.txt'])
```

## Nested Patterns

Patterns can be nested inside other patterns. This is where structural  
matching becomes especially useful: one pattern can describe several  
levels of a data structure at once.

```python
# nested.py

data = [
    ("user", {"id": 1, "role": "admin"}),
    ("user", {"id": 2, "role": "editor"}),
    ("guest", {"token": "abc123"}),
]

for item in data:
    match item:
        case ("user", {"role": "admin", "id": user_id}):
            print(f"Admin user with id {user_id}")
        case ("user", {"role": "editor"}):
            print("Editor user")
        case ("guest", {"token": token}):
            print(f"Guest with token {token}")
        case _:
            print("Unknown item")
```

The pattern is a two-item tuple whose second item is a mapping. The  
mapping pattern then matches the `"role"` key and binds `id` or `token`.

```text
$ python nested.py
Admin user with id 1
Editor user
Guest with token abc123
```

## Common Mistakes

### A bare name captures instead of comparing

A bare name in a pattern always captures. It never reads an existing  
variable with the same spelling.

```python
# capture_vs_compare.py

lang = "slovak"
german = "german"

match lang:
    case german:
        print(f"matched {german}")
```

```text
$ python capture_vs_compare.py
matched slovak
```

The `german` in the pattern is a new name that captures `"slovak"`; it  
does not compare with the variable defined above. The print confirms  
this. To compare with a variable, use a guard:

```python
# capture_fixed.py

lang = "slovak"
german = "german"

match lang:
    case value if value == german:
        print("matched German")
    case _:
        print("not German")
```

```text
$ python capture_fixed.py
not German
```

When the value is known in advance, a literal pattern such as  
`case "german":` is simpler. For named constants, a value pattern such  
as `case Day.Monday:` keeps the dot that prevents capture.

### Patterns are not expressions

A pattern is not an ordinary expression, so a comparison cannot appear  
directly after `case`.

```python
# expr_pattern.py

match 5:
    case n > 0:
        print("positive")
```

```text
$ python expr_pattern.py
  File ".../expr_pattern.py", line 4
    case n > 0:
           ^
SyntaxError: invalid syntax
```

Write the comparison as a guard instead: `case n if n > 0:`. For  
alternatives, use the vertical bar (`case "A" | "B":`), not the word  
`or`.

### The wildcard must be last

```python
# wildcard_last.py

match 5:
    case _:
        print("any number")
    case 5:
        print("five")
```

```text
$ python wildcard_last.py
  File ".../wildcard_last.py", line 4
    case _:
         ^
SyntaxError: wildcard makes remaining patterns unreachable
```

Python reports the problem while compiling the file, before any code  
runs.

### A name cannot be bound twice in one pattern

```python
# duplicate_name.py

match [1, 2]:
    case [x, x]:
        print(x)
```

```text
$ python duplicate_name.py
  File ".../duplicate_name.py", line 4
    case [x, x]:
             ^
SyntaxError: multiple assignments to name 'x' in pattern
```

`[x, x]` asks for the same name twice, which is ambiguous. Use two  
different names and compare them in a guard instead:  
`case [x, y] if x == y:`.

### Parentheses do not create a tuple pattern

```python
# parentheses.py

match "quit":
    case ("quit"):
        print("parentheses group, they do not create a tuple")
```

```text
$ python parentheses.py
parentheses group, they do not create a tuple
```

`("quit")` is just the string `"quit"` in parentheses. For a one-item  
tuple pattern write `("quit",)`, and for a one-item list pattern write  
`["quit"]`. This matters when the subject is a tuple or a list, as in  
the `split()` examples.

### Positional patterns need `__match_args__`

```python
# positional_error.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match Point(1, 2):
    case Point(a, b):
        print(a, b)
```

```text
$ python positional_error.py
Traceback (most recent call last):
  File ".../positional_error.py", line 9, in <module>
    case Point(a, b):
         ~~~~~^^^^^^
TypeError: Point() accepts 0 positional sub-patterns (2 given)
```

The class has no `__match_args__`, so Python does not know which  
attributes the two positional values should match. Add  
`__match_args__ = ("x", "y")` to the class, or use keyword patterns such  
as `case Point(x=a, y=b):`.

### When no arm matches

A `match` statement with no matching arm produces no output and no error.  
Execution simply continues after it.

```python
# no_match.py

match "maybe":
    case "yes":
        print("yes")
    case "no":
        print("no")

print("after match")
```

```text
$ python no_match.py
after match
```

If the `match` is supposed to handle every possible value, add a final  
wildcard arm or an arm that raises `ValueError`.

## Hands-On: A Small Command Parser

The final example combines sequences, star patterns, guards, and the  
wildcard. It reads simple text commands and dispatches them.

```python
# commands.py

commands = [
    "quit",
    "move 10 20",
    "move 5",
    "say hello world",
    "jump",
    "",
]

for command in commands:
    match command.split():
        case ["quit"]:
            print("bye")
        case ["move", x, y] if x.isdigit() and y.isdigit():
            print(f"move to ({int(x)}, {int(y)})")
        case ["move", *_]:
            print(f"invalid move: {command!r}")
        case ["say", *words] if words:
            print("say:", " ".join(words))
        case _:
            print(f"unknown command: {command!r}")
```

`command.split()` produces the subject list. The first arm matches the  
single word `"quit"`. The second arm requires two non-negative integer  
arguments and checks them with a guard. The third arm catches any other  
`"move"` command, and `["say", *words]` collects the remaining words.

```text
$ python commands.py
bye
move to (10, 20)
invalid move: 'move 5'
say: hello world
unknown command: 'jump'
unknown command: ''
```

Each pattern describes the shape of the command. The same logic with  
`if/elif` would need nested length checks and indexing.

Pattern matching is not always the best tool. For one or two simple  
conditions, `if/elif` is shorter. Reach for `match` when the shape of the  
data matters or when several alternatives should share one block.

## Summary

| Feature | Matches | Example |
| --- | --- | --- |
| Literal | A value equal to the literal | `case 404:` |
| Value | A named constant, such as an enum member | `case Day.Monday:` |
| OR pattern | Any of the alternatives | `case "A" \| "B":` |
| Wildcard | Anything, binds nothing | `case _:` |
| Capture | Anything, binds a name | `case value:` |
| Guard | A pattern plus a true condition | `case n if n < 0:` |
| Sequence | A sequence of fixed length | `case [x, y]:` |
| Star sequence | A sequence of variable length | `case [first, *rest]:` |
| Mapping | A dictionary with at least the given keys | `case {"id": id}:` |
| Class | An instance of a class | `case Point(x, y):` |
| `as` | A pattern plus the whole value | `case [x] as pair:` |

The first matching arm wins, so order patterns from the most specific to  
the most general.

## References

- [PEP 634: Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)
- [PEP 635: Structural Pattern Matching: Motivation and Rationale](https://peps.python.org/pep-0635/)
- [PEP 636: Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
- [The Python Tutorial: match Statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [The Python Language Reference: The match statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
- [What's New in Python 3.10](https://docs.python.org/3/whatsnew/3.10.html)
