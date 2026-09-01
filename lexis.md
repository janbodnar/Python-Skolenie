# Lexical Structure of Python

Lexical structure describes how Python source code is divided into the smallest meaningful units. These units are called **tokens**. The parser uses tokens to understand the structure of a program.

The main lexical elements are:

- **Identifiers**: names of variables, functions, classes, and modules
- **Keywords**: reserved words with a special meaning
- **Literals**: values written directly in source code
- **Operators**: symbols and words that combine, compare, or transform values
- **Delimiters**: punctuation that groups or separates parts of an expression
- **Comments**: source text ignored by the parser
- **Indentation and line breaks**: whitespace that can affect block structure

Variables are not a separate token category. A variable is a name, or identifier, bound to an object. Assignment is an operation that creates or changes that binding.

## Comments

A **comment** is source text intended for human readers. Python ignores everything from `#` to the end of the physical line, except when the `#` occurs inside a string literal.

```python
# A comment on its own line
print("Hello")  # A comment after a statement
```

Python has no dedicated multi-line comment syntax. For a longer comment, use several `#` lines:

```python
# This function demonstrates a small calculation.
# The comment explains the purpose of the code,
# rather than repeating what each line does.
def calculate_area(radius):
    return 3.14159 * radius ** 2
```

### Comments and docstrings

Triple-quoted text is a **string literal**, not a comment. When it is the first statement in a module, class, or function, it becomes that object's docstring and is available through `__doc__`.

```python
def calculate_area(radius):
    """Return the area of a circle with the given radius."""
    return 3.14159 * radius ** 2
```

Use comments to explain intent or a non-obvious decision. Use docstrings to document public modules, classes, and functions. Keep both current when the code changes.

## Identifiers and Variables

An **identifier** is a name used to identify an object or program element. Python names are case-sensitive: `name`, `Name`, and `NAME` are different identifiers.

### Naming rules

Identifiers may contain Unicode letters, decimal digits, and underscores, but an identifier cannot start with a digit. In normal Python code, ASCII letters and underscores are the clearest choice.

An identifier cannot be a keyword. The following examples show valid and invalid forms:

```python
value = 10
value2 = 20
company_name = "Acme"
_internal_name = "implementation detail"
MAX_CONNECTIONS = 100

12value = 10       # SyntaxError: cannot start with a digit
first-name = "A"   # Parsed as subtraction, not as one identifier
class = "Math"     # SyntaxError: class is a keyword
```

### Naming conventions

PEP 8 recommends these conventions:

- Functions and variables: `snake_case`, such as `user_age`
- Constants: `UPPER_SNAKE_CASE`, such as `MAX_CONNECTIONS`
- Classes: `CapWords`, such as `UserProfile`
- Internal names: a leading underscore, such as `_cache`

### Names and objects

Python variables do not contain values directly. A name refers to an object, and assignment binds the name to that object:

```python
value = 10
value = "Hello"  # The same name now refers to a string object
value = [1, 2, 3]
```

The type belongs to the object, not permanently to the name. This is why Python is described as dynamically typed.

```python
number = 10
Number = 11
NUMBER = 12

print(number, Number, NUMBER)  # 10 11 12
```

Although different capitalization is legal, related names should normally follow one consistent convention.

## Literals

A **literal** is notation that creates a value directly in source code. Literal syntax is part of the program; the resulting objects are created when the relevant code executes. Details such as constant folding are implementation details and should not be relied on.

| Type | Examples |
| --- | --- |
| Numeric | `42`, `3.14`, `0b1010`, `0o755`, `0xFF` |
| String | `"Hello"`, `'World'`, `"""Multiline"""` |
| Boolean | `True`, `False` |
| None | `None` |
| Collection | `[1, 2, 3]`, `{"a": 1}`, `(1, 2, 3)`, `{1, 2, 3}` |

```python
age = 29
nationality = "Slovak"
is_student = True
coordinates = (10, 20)
missing_value = None
```

An expression containing only a literal has no lasting effect in a script unless the value is used. In the interactive interpreter, however, the result of an expression is displayed, and a string literal in the first position of a module, class, or function can become a docstring.

```python
"unused in a script"
42

name = "Jane"
print(name)  # Jane
```

## Operators

**Operators** combine or transform operands. Some operators use symbols, while others use keywords such as `and`, `in`, and `is`.

| Category | Operators |
| --- | --- |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | `and`, `or`, `not` |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `\|=`, `^=`, `>>=`, `<<=` |
| Identity | `is`, `is not` |
| Membership | `in`, `not in` |

### Operator precedence

From higher to lower precedence, the most common groups are:

1. Parentheses and subscription or call expressions, such as `()` and `[]`
2. Exponentiation: `**`
3. Unary operators: `+x`, `-x`, `~x`
4. Multiplication and division: `*`, `/`, `//`, `%`
5. Addition and subtraction: `+`, `-`
6. Shifts: `<<`, `>>`
7. Bitwise `&`, `^`, and `|`
8. Comparisons, identity, and membership
9. `not`, then `and`, then `or`

When an expression is important or complex, use parentheses to make the intended grouping explicit.

```python
x = 10 + 5 * 2       # 20
y = (10 + 5) * 2     # 30
is_equal = 5 == 5    # True
```

## Indentation and Line Structure

Python uses indentation to represent the nesting of compound statements. A colon introduces a suite, and the following indented lines form that suite.

```python
age = 34

if age >= 18:
    print("Adult")
    if age >= 65:
        print("Retired age")

print("Done")
```

Use four spaces per indentation level, as recommended by PEP 8. Do not mix tabs and spaces in the same block. Inconsistent indentation can raise `IndentationError` or `TabError`.

Blank lines and comments do not create or close a block. Python's tokenizer turns changes in indentation into `INDENT` and `DEDENT` tokens. Line breaks can also produce `NEWLINE` tokens, while a backslash or open bracket can continue a logical line.

```python
# ERROR: the suite after the colon must be indented
if condition:
print("This raises IndentationError")
```

## Delimiters

**Delimiters** are punctuation marks that group or separate syntactic elements. Their exact role depends on the surrounding syntax.

| Role | Delimiters and examples |
| --- | --- |
| Grouping and calls | `(...)` |
| Lists, indexing, and slices | `[...]`, `data[1:10]` |
| Dictionaries, sets, and set displays | `{...}` |
| Separating items | `,` |
| Starting suites and separating keys from values | `:` |
| Attribute access | `.` |
| Statement separator | `;` |
| Decorator marker | `@` |

```python
result = (2 + 3) * 4
colors = ["red", "green", "blue"]
first_color = colors[0]
person = {"name": "John", "age": 30}
numbers = {1, 2, 3}

if result > 0:
    print(person["name"])

@staticmethod
def describe():
    return "example"
```

Assignment operators and arithmetic operators belong to the operator category, even though they use punctuation. Quotes introduce string literals, and a backslash is an escape character inside a string or a line-continuation marker in specific contexts; neither is a general-purpose delimiter.

## Keywords

**Keywords** are reserved identifiers with a predefined meaning. They cannot be used as ordinary variable, function, or class names.

The exact list depends on the Python version. In current Python versions, the hard keywords are:

```text
and       as        assert    async     await     break
class     continue  def       del       elif      else
except    False     finally   for       from      global
if        import    in        is        lambda    None
nonlocal  not       or        pass      raise     return
True      try       while     with      yield
```

Python also has **soft keywords**. `match` and `case` have special meaning in pattern matching, `_` can be a wildcard pattern, and `type` has a special meaning in type-alias statements. Their special meaning depends on context, so use `keyword.softkwlist` to inspect the interpreter you are running.

```python
import keyword

print(keyword.kwlist)                 # Hard keywords
print(keyword.softkwlist)              # Context-dependent keywords
print(keyword.iskeyword("class"))     # True
print(keyword.iskeyword("my_var"))    # False
print(keyword.issoftkeyword("type"))  # Version-dependent
```

The programmatic approach is preferable when writing tools because keyword lists can change between Python releases.

## Summary

| Element | Meaning | Examples |
| --- | --- | --- |
| Comments | Text ignored by the parser | `# explanation` |
| Identifiers | Names used by a program | `user_name`, `calculate_area` |
| Literals | Values written directly in code | `42`, `"Hello"`, `True` |
| Operators | Symbols or words that operate on values | `+`, `==`, `and` |
| Delimiters | Punctuation that groups or separates syntax | `()`, `[]`, `{}`, `,`, `:` |
| Indentation | Whitespace that represents block nesting | `INDENT`, `DEDENT` |
| Keywords | Reserved or context-dependent language words | `if`, `def`, `match`, `case` |

## References

- [Python Language Reference: Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html)
- [Python Language Reference: Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
- [Python Standard Library: `keyword`](https://docs.python.org/3/library/keyword.html)
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/)