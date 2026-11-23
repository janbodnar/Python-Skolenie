# Lexical Structure of Python

The lexical structure of a language describes how source code is split into its  
smallest meaningful units, called **tokens**. Before Python can run a program,  
the tokenizer reads the source text and turns it into a stream of tokens. The  
parser then uses these tokens to build the structure of the program.

Python recognizes these main lexical elements:

- **Identifiers**: names of variables, functions, classes, and modules
- **Keywords**: reserved words with a special meaning
- **Literals**: values written directly in source code
- **Operators**: symbols and words that combine, compare, or transform values
- **Delimiters**: punctuation that groups or separates parts of the code
- **Comments**: text for human readers that the tokenizer discards
- **Line structure and indentation**: line breaks and leading whitespace that  
  define statements and blocks

Variables are not a separate token category. A variable is a name (an  
identifier) bound to an object. Assignment is the operation that creates or  
changes that binding.

At the end of this chapter, you will use the `tokenize` module to see the  
tokens of a complete program.

## Comments

A **comment** is source text intended for human readers. Python ignores  
everything from `#` to the end of the physical line, unless the `#` appears  
inside a string literal.

```python
# A comment on its own line
print("Hello")  # A comment after a statement
print("# This is not a comment, it is part of the string")
```

Python has no dedicated multi-line comment syntax. For a longer comment, use  
several lines that each start with `#`:

```python
# Calculate the area of a circle.
# math.pi is used instead of a hard-coded approximation
# so that the result is as precise as a float allows.
import math

def calculate_area(radius):
    return math.pi * radius ** 2
```

### Comments and docstrings

Triple-quoted text is a **string literal**, not a comment. When a string literal  
is the first statement in a module, class, or function, it becomes that object's  
**docstring** and is available through the `__doc__` attribute and the `help()`  
function.

```python
import math

def calculate_area(radius):
    """Return the area of a circle with the given radius."""
    return math.pi * radius ** 2

print(calculate_area.__doc__)  # Return the area of a circle ...
```

Use comments to explain intent or a non-obvious decision, not to repeat what the  
code already says. Use docstrings to document public modules, classes, and  
functions. Keep both up to date when the code changes; an outdated comment is  
worse than none.

## Identifiers

An **identifier** is a name that refers to a variable, function, class, module,  
or other program element.

### Naming rules

- An identifier may contain letters, decimal digits, and underscores.
- It cannot start with a digit.
- It cannot be a hard keyword such as `class` or `for`.
- Identifiers are case-sensitive: `name`, `Name`, and `NAME` are three different  
  names.

Python accepts non-ASCII letters in identifiers, so `výška` is a valid name,  
while `cena€` is not, because `€` is not a letter. In practice, ASCII letters  
are the most portable and readable choice.

```python
value = 10
value2 = 20
company_name = "Acme"
_internal_name = "implementation detail"
MAX_CONNECTIONS = 100
výška = 182          # Valid, but ASCII names are preferred

12value = 10         # SyntaxError: cannot start with a digit
first-name = "A"     # SyntaxError: parsed as first - name
class = "Math"       # SyntaxError: class is a keyword
```

Case sensitivity is easy to demonstrate:

```python
number = 10
Number = 11
NUMBER = 12

print(number, Number, NUMBER)  # 10 11 12
```

This is legal, but names that differ only in capitalization are confusing. Avoid  
them in real code.

### Naming conventions

PEP 8, the official style guide, recommends these conventions:

| Kind of name | Convention | Example |
| --- | --- | --- |
| Variables and functions | `snake_case` | `user_age`, `load_data` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_CONNECTIONS` |
| Classes | `CapWords` | `UserProfile` |
| Internal (non-public) names | leading underscore | `_cache` |
| Special (dunder) names | double underscores on both sides | `__init__`, `__name__` |

Names with double underscores on both sides are reserved for Python itself. Use  
the existing ones, such as `__init__`, but do not invent new ones.

### Names and objects

A Python variable does not contain a value directly. It is a name that refers to  
an object, and assignment binds the name to that object:

```python
value = 10           # value refers to an int object
value = "Hello"      # The same name now refers to a str object
value = [1, 2, 3]    # ... and now to a list object
```

The type belongs to the object, not to the name. A name can refer to objects of  
different types over time, which is why Python is described as **dynamically  
typed**.

## Keywords

**Keywords** are reserved words with a predefined meaning. Hard keywords cannot  
be used as names of variables, functions, classes, or anything else.

In current Python versions, the hard keywords are:

```text
False     None      True      and       as        assert
async     await     break     class     continue  def
del       elif      else      except    finally   for
from      global    if        import    in        is
lambda    nonlocal  not       or        pass      raise
return    try       while     with      yield
```

Python also has **soft keywords**. They have a special meaning only in specific  
contexts and remain ordinary identifiers everywhere else:

- `match`, `case`, and `_` in structural pattern matching (Python 3.10+)
- `type` in type alias statements (Python 3.12+)
- `lazy` in lazy import statements (Python 3.15+)

```python
match = "a valid variable name"  # Legal, but not recommended

type Point = tuple[float, float]  # Here, type is a soft keyword
```

The exact keyword lists depend on the Python version. Use the `keyword` module  
to inspect the interpreter you are running:

```python
import keyword

print(keyword.kwlist)                 # Hard keywords
print(keyword.softkwlist)             # Soft keywords
print(keyword.iskeyword("class"))     # True
print(keyword.iskeyword("my_var"))    # False
print(keyword.issoftkeyword("type"))  # True in Python 3.12+
```

The programmatic approach is preferable when writing tools, such as code  
generators or linters, because the lists change between releases.

## Literals

A **literal** is notation that represents a fixed value directly in source code.

| Type | Examples |
| --- | --- |
| Integer | `42`, `1_000_000`, `0b1010`, `0o755`, `0xFF` |
| Floating point | `3.14`, `.5`, `1e-3`, `2.5E6` |
| Imaginary | `3j`, `1.5j` |
| String | `"Hello"`, `'World'`, `"""Multiline"""`, `r"C:\temp"`, `f"{x}"` |
| Bytes | `b"data"`, `b'\x00\xff'` |

A few details are worth knowing:

- Underscores can group digits for readability: `1_000_000` equals `1000000`.
- A leading minus sign is not part of a numeric literal. `-5` is the unary  
  operator `-` applied to the literal `5`.
- Adjacent string literals are joined at compile time: `"Hello, " "World"` is  
  the same as `"Hello, World"`.
- f-strings (`f"..."`) look like literals, but they contain expressions that are  
  evaluated at run time.

Some values that look like literals are tokenized differently:

- `True`, `False`, and `None` are keywords. They behave like constant values and  
  cannot be reassigned.
- `[1, 2, 3]`, `{"a": 1}`, and `{1, 2, 3}` are **displays**, not literals. They  
  are expressions that build a new list, dictionary, or set each time they run.
- A tuple is created by commas, not by parentheses: `1, 2, 3` is already a  
  tuple. Parentheses only group it, and `()` creates an empty tuple.

```python
age = 29
nationality = "Slovak"
population = 5_400_000
ratio = 0.75
is_student = True
missing_value = None
coordinates = (10, 20)          # Tuple created by the comma
greeting = "Hello, " "World"    # "Hello, World"
```

A literal on its own line is a valid expression statement, but in a script its  
value is computed and then discarded. In the interactive interpreter, the value  
of such an expression is displayed instead.

```python
42                 # No effect in a script; prints 42 in the REPL

name = "Jane"
print(name)        # Jane
```

## Operators

**Operators** combine or transform values, called **operands**. Most operators  
are symbols, but some are keywords such as `and`, `in`, and `is`.

| Category | Operators |
| --- | --- |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `@` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | `and`, `or`, `not` |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` |
| Identity | `is`, `is not` |
| Membership | `in`, `not in` |
| Assignment expression | `:=` |

The `@` operator is used for matrix multiplication, for example by NumPy arrays.  
The `:=` operator, nicknamed the walrus operator, assigns a value inside an  
expression:

```python
data = [3, 8, 1, 9]

if (n := len(data)) > 3:
    print(f"List is too long ({n} elements)")
```

### Assignment

The ordinary assignment `=` and augmented assignments such as `+=`, `-=`, `*=`,  
`/=`, `//=`, `%=`, `**=`, `@=`, `&=`, `|=`, `^=`, `<<=`, and `>>=` are often  
called assignment operators. Formally, the language reference lists them as  
delimiters, because assignment is a statement, not an expression that produces a  
value.

```python
count = 0
count += 1       # Same as count = count + 1 for numbers
print(count)     # 1
```

### Operator precedence

Operators with higher precedence are evaluated first. From highest to lowest,  
the most common groups are:

1. Calls, indexing, slicing, and attribute access: `f(x)`, `a[i]`, `a[1:3]`,  
   `obj.attr`
2. `await`
3. Exponentiation: `**`
4. Unary operators: `+x`, `-x`, `~x`
5. Multiplication and division: `*`, `@`, `/`, `//`, `%`
6. Addition and subtraction: `+`, `-`
7. Shifts: `<<`, `>>`
8. Bitwise AND: `&`
9. Bitwise XOR: `^`
10. Bitwise OR: `|`
11. Comparisons, identity, and membership: `==`, `<`, `is`, `in`, ...
12. Logical `not`
13. Logical `and`
14. Logical `or`
15. Conditional expression: `x if condition else y`
16. `lambda`
17. Assignment expression: `:=`

Parenthesized expressions are always evaluated first, so use parentheses  
whenever the intended grouping is not obvious.

```python
x = 10 + 5 * 2       # 20
y = (10 + 5) * 2     # 30
z = -2 ** 2          # -4, because ** binds tighter than unary minus
w = (-2) ** 2        # 4
is_equal = 5 == 5    # True
```

Most operators are evaluated from left to right. Exponentiation is the  
exception: it groups from right to left, so `2 ** 3 ** 2` means `2 ** (3 ** 2)`,  
which is `512`.

Comparisons can be chained. `0 < x < 10` means `0 < x and x < 10`, except that  
`x` is evaluated only once.

## Delimiters

**Delimiters** are punctuation marks that group or separate parts of the code.  
Their exact role depends on the surrounding syntax.

| Delimiter | Typical role | Example |
| --- | --- | --- |
| `( )` | Grouping, calls, tuples | `(a + b) * c`, `print(x)` |
| `[ ]` | Lists, indexing, slicing | `[1, 2]`, `data[0]`, `data[1:10]` |
| `{ }` | Dictionaries and sets | `{"a": 1}`, `{1, 2}` |
| `,` | Separating items and arguments | `f(a, b)` |
| `:` | Starting a block, dict keys, slices, annotations | `if x:`, `{"a": 1}`, `x: int` |
| `.` | Attribute access | `text.upper()` |
| `;` | Separating statements on one line | `a = 1; b = 2` |
| `@` | Decorator | `@functools.cache` |
| `->` | Return type annotation | `def f() -> int:` |
| `=` | Assignment, default and keyword arguments | `x = 1`, `f(end="")` |

```python
import functools

result = (2 + 3) * 4
colors = ["red", "green", "blue"]
first_color = colors[0]
person = {"name": "John", "age": 30}
numbers = {1, 2, 3}

if result > 0:
    print(person["name"])

@functools.cache
def square(n: int) -> int:
    return n * n
```

Avoid the semicolon in everyday code. PEP 8 recommends one statement per line.

Some characters are neither operators nor delimiters. Quotes start and end  
string literals, `#` starts a comment, and the backslash `\` is an escape  
character inside strings or a line-continuation marker at the end of a line.

## Line Structure and Indentation

### Logical and physical lines

A **physical line** is a line of text in the source file. A **logical line** is  
one complete statement, and the tokenizer marks its end with a `NEWLINE` token.  
Normally, one physical line is one logical line.

A logical line can span several physical lines in two ways. **Implicit line  
joining** happens inside parentheses, brackets, and braces. This is the  
preferred way to split long lines:

```python
total = (price * quantity
         + shipping_cost
         - discount)

colors = [
    "red",
    "green",
    "blue",
]
```

**Explicit line joining** uses a backslash at the end of a line. It is fragile,  
because a single space after the backslash breaks it, so prefer brackets:

```python
total = price * quantity \
        + shipping_cost
```

Blank lines and lines that contain only a comment are ignored by the parser.

### Indentation

Python uses indentation, not braces, to group statements into blocks. A compound  
statement such as `if`, `for`, `def`, or `class` ends its header with a colon.  
The indented lines that follow form its body, also called a **suite**.

```python
age = 70

if age >= 18:
    print("Adult")
    if age >= 65:
        print("Retirement age")

print("Done")
```

The tokenizer turns increases in indentation into `INDENT` tokens and decreases  
into `DEDENT` tokens. To the parser, these tokens play the same role that `{`  
and `}` play in C or Java.

Use four spaces per indentation level, as recommended by PEP 8. Do not mix tabs  
and spaces. Inconsistent indentation raises `IndentationError` or its subclass  
`TabError`.

```python
# Error: the body after the colon must be indented
if age >= 18:
print("Adult")       # IndentationError: expected an indented block
```

A block must contain at least one statement. When you need an empty block, use  
`pass`:

```python
def not_implemented_yet():
    pass
```

## Seeing the Tokens

The standard `tokenize` module shows how Python splits a source file into  
tokens. It is a good way to check everything this chapter describes. Save the  
following program as `area.py`:

```python
# Compute the areas of several circles.
import math


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


radii = [1, 2.5, 4]

for r in radii:
    if r > 2:
        print(f"r={r}", round(circle_area(r), 2))
```

The next script reads a Python file given on the command line and prints every  
token with its position (line and column), type, and text. `tokenize.open`  
opens the file in the correct encoding, and `generate_tokens` produces the  
tokens one by one:

```python
import sys
import tokenize

file_name = sys.argv[1]

with tokenize.open(file_name) as f:
    for tok in tokenize.generate_tokens(f.readline):
        row, col = tok.start
        name = tokenize.tok_name[tok.type]
        print(f"{row:>2}:{col:<3} {name:<14} {tok.string!r}")
```

Run the script with the file name as an argument:

```text
$ python show_tokens.py area.py
 1:0   COMMENT        '# Compute the areas of several circles.'
 1:39  NL             '\n'
 2:0   NAME           'import'
 2:7   NAME           'math'
 2:11  NEWLINE        '\n'
 3:0   NL             '\n'
 4:0   NL             '\n'
 5:0   NAME           'def'
 5:4   NAME           'circle_area'
 5:15  OP             '('
 5:16  NAME           'radius'
 5:22  OP             ')'
 5:23  OP             ':'
 5:24  NEWLINE        '\n'
 6:0   INDENT         '    '
 6:4   STRING         '"""Return the area of a circle."""'
 6:38  NEWLINE        '\n'
 7:4   NAME           'return'
 7:11  NAME           'math'
 7:15  OP             '.'
 7:16  NAME           'pi'
 7:19  OP             '*'
 7:21  NAME           'radius'
 7:28  OP             '**'
 7:31  NUMBER         '2'
 7:32  NEWLINE        '\n'
 8:0   NL             '\n'
 9:0   NL             '\n'
10:0   DEDENT         ''
10:0   NAME           'radii'
10:6   OP             '='
10:8   OP             '['
10:9   NUMBER         '1'
10:10  OP             ','
10:12  NUMBER         '2.5'
10:15  OP             ','
10:17  NUMBER         '4'
10:18  OP             ']'
10:19  NEWLINE        '\n'
11:0   NL             '\n'
12:0   NAME           'for'
12:4   NAME           'r'
12:6   NAME           'in'
12:9   NAME           'radii'
12:14  OP             ':'
12:15  NEWLINE        '\n'
13:0   INDENT         '    '
13:4   NAME           'if'
13:7   NAME           'r'
13:9   OP             '>'
13:11  NUMBER         '2'
13:12  OP             ':'
13:13  NEWLINE        '\n'
14:0   INDENT         '        '
14:8   NAME           'print'
14:13  OP             '('
14:14  FSTRING_START  'f"'
14:16  FSTRING_MIDDLE 'r='
14:18  OP             '{'
14:19  NAME           'r'
14:20  OP             '}'
14:21  FSTRING_END    '"'
14:22  OP             ','
14:24  NAME           'round'
14:29  OP             '('
14:30  NAME           'circle_area'
14:41  OP             '('
14:42  NAME           'r'
14:43  OP             ')'
14:44  OP             ','
14:46  NUMBER         '2'
14:47  OP             ')'
14:48  OP             ')'
14:49  NEWLINE        '\n'
15:0   DEDENT         ''
15:0   DEDENT         ''
15:0   ENDMARKER      ''
```

The output illustrates several points from this chapter:

- Keywords such as `import`, `def`, `for`, and `if` are reported as `NAME`  
  tokens. The tokenizer does not distinguish them from identifiers; the parser  
  does.
- Operators and delimiters share the `OP` token type, for example `**`, `=`,  
  `(`, and `:`.
- The comment becomes a single `COMMENT` token, and the docstring is an  
  ordinary `STRING` token. The `tokenize` module keeps comments so that tools  
  such as formatters can work with them; the parser never sees them.
- `NEWLINE` ends a logical line, while `NL` marks a line break that does not  
  end a statement, such as a blank line or a line containing only a comment.
- Each increase in indentation produces an `INDENT` token and each decrease a  
  `DEDENT` token. At the end of the file, both open blocks are closed by two  
  `DEDENT` tokens.
- Since Python 3.12, an f-string is split into `FSTRING_START`,  
  `FSTRING_MIDDLE`, and `FSTRING_END` tokens, with the embedded expression  
  `{r}` tokenized as normal code.

## Summary

| Element | Meaning | Examples |
| --- | --- | --- |
| Comments | Text for readers, discarded by the tokenizer | `# explanation` |
| Identifiers | Names that refer to objects | `user_name`, `calculate_area` |
| Keywords | Reserved words; soft keywords depend on context | `if`, `def`, `match`, `type` |
| Literals | Values written directly in code | `42`, `3.14`, `"Hello"`, `b"data"` |
| Operators | Symbols or words that operate on values | `+`, `==`, `and`, `:=` |
| Delimiters | Punctuation that groups or separates code | `()`, `[]`, `{}`, `,`, `:` |
| Line structure | Logical lines and indentation-based blocks | `NEWLINE`, `INDENT`, `DEDENT` |

## References

- [Python Language Reference: Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html)
- [Python Language Reference: Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Python Standard Library: `keyword`](https://docs.python.org/3/library/keyword.html)
- [Python Standard Library: `tokenize`](https://docs.python.org/3/library/tokenize.html)
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/)
