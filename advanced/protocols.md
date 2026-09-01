# Python Protocols: A Complete Tutorial

Protocols, introduced in **PEP 544** (Python 3.8) and available via `typing.Protocol`,
bring **structural subtyping** to Python's static type system. They let you define a set
of methods or attributes that a class must provide – without requiring explicit
inheritance. This is *duck typing* made explicit and checkable by tools like `mypy` and
`pyright`.

Every code block in this tutorial is **standalone and runnable**. Copy any example into
a `.py` file and run it directly to see the output.

**Topics covered:**

1. What protocols are and why they matter
2. Defining a protocol
3. Using a protocol as a type hint
4. Implicit vs. explicit subtyping
5. Runtime checks with `@runtime_checkable`
6. Combining protocols (inheritance)
7. Generic protocols
8. Recursive protocols
9. Protocols vs. Abstract Base Classes
10. Practical use cases: dependency injection, callables, repository pattern
11. Advanced patterns: `TypeVar` bounds, self-type, async, class/static methods
12. Common pitfalls
13. Best practices
14. Summary


---

## 1. What Are Protocols?

In traditional OOP, **nominal subtyping** requires explicit inheritance:
`class Dog(Animal)` makes `Dog` a subtype of `Animal`. Python also embraces
**duck typing**: *"If it walks like a duck and quacks like a duck, it's a duck."*
The type checker traditionally had no way to verify this at analysis time — only
runtime errors revealed the problem.

**Protocols** bridge this gap. They describe an expected interface (a set of
methods/attributes), and any class that provides that interface is considered a
structural subtype — **without** inheriting from it.

```python
# example_proto_minimal.py
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Circle drawn")

class Square:
    def draw(self) -> None:
        print("Square drawn")

def render(obj: Drawable) -> None:
    obj.draw()

if __name__ == "__main__":
    render(Circle())  # Circle drawn
    render(Square())  # Square drawn
```

Output:
```
Circle drawn
Square drawn
```

`Circle` and `Square` never inherit `Drawable`, but they satisfy its structure, so a
static type checker accepts them wherever `Drawable` is expected.


---

## 2. Defining a Protocol

A protocol is a subclass of `typing.Protocol`. Its body contains **method stubs**
(bodies are `...` or `pass`) and **attribute annotations** (no assigned value).

```python
# example_proto_attributes.py
from typing import Protocol

class Named(Protocol):
    name: str                              # attribute expected
    def greet(self, greeting: str) -> str: ...

class User:
    name: str = "Alice"
    def greet(self, greeting: str) -> str:
        return f"{greeting}, I'm {self.name}"

def log_named(obj: Named) -> None:
    print(f"Object name: {obj.name} - {obj.greet('Hi')}")

if __name__ == "__main__":
    log_named(User())
```

Output:
```
Object name: Alice - Hi, I'm Alice
```

Protocol members can be:

| Member type       | Syntax                                |
|-------------------|---------------------------------------|
| Instance method   | `def method(self) -> T: ...`          |
| Class method      | `@classmethod` + `def cm(cls) -> T: ...` |
| Static method     | `@staticmethod` + `def sm() -> T: ...` |
| Property          | `@property` + `def prop(self) -> T: ...` |
| Attribute         | `name: T` (annotation only)           |

```python
from typing import Protocol

class HasArea(Protocol):
    @property
    def area(self) -> float: ...

    @classmethod
    def from_dimensions(cls, dims: tuple) -> 'HasArea': ...
```

Default implementations *can* appear in protocols — explicit subclasses inherit
them, but they are **not required** for structural subtyping.


---

## 3. Using a Protocol as a Type Hint

Once defined, use a protocol anywhere a type is expected: function parameters,
return types, class attributes, etc.

```python
# example_proto_type_hint.py
from typing import Protocol

class Serializable(Protocol):
    def to_json(self) -> dict: ...

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    def to_json(self) -> dict:
        return {"name": self.name, "price": self.price}

class Order:
    def __init__(self, order_id: int, total: float):
        self.order_id = order_id
        self.total = total
    def to_json(self) -> dict:
        return {"order_id": self.order_id, "total": self.total}

def save(obj: Serializable) -> str:
    import json
    return json.dumps(obj.to_json())

if __name__ == "__main__":
    print(save(Product("Widget", 9.99)))
    print(save(Order(42, 29.97)))
```

Output:
```
{"name": "Widget", "price": 9.99}
{"order_id": 42, "total": 29.97}
```

A type checker verifies that every concrete class passed to `save` has a `to_json`
method with a compatible signature.


---

## 4. Implicit vs. Explicit Subtyping

Structural subtyping is **implicit**: a class satisfies a protocol simply by having
the required members, without declaring any inheritance.

```python
# example_proto_implicit_explicit.py
from typing import Protocol

class Named(Protocol):
    name: str
    def greet(self, greeting: str) -> str: ...

# Implicit – no inheritance declared
class Dog:
    name: str = "Rex"
    def greet(self, greeting: str) -> str:
        return f"{greeting}, I'm {self.name}"

# Explicit – inherits the protocol (nominal + structural)
class Cat(Named):
    name: str = "Whiskers"
    def greet(self, greeting: str) -> str:
        return f"{greeting}, I'm {self.name}"

def introduce(obj: Named) -> None:
    print(obj.greet("Hello"))

if __name__ == "__main__":
    introduce(Dog())   # Hello, I'm Rex
    introduce(Cat())   # Hello, I'm Whiskers
```

Output:
```
Hello, I'm Rex
Hello, I'm Whiskers
```

**Advantages of implicit subtyping:**

- Decouples libraries from user code.
- Enables *retroactive typing*: define a protocol for existing classes (even from
  third-party libraries) without touching them.
- Encourages small, focused interfaces (interface segregation principle).


---

## 5. Runtime Checks with `@runtime_checkable`

By default, `isinstance(obj, SomeProtocol)` raises `TypeError`. Decorate a protocol
with `@runtime_checkable` to enable a limited runtime check.

```python
# example_proto_runtime.py
from typing import runtime_checkable, Protocol

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

class Tree:
    def draw(self) -> None:
        print("Drawing tree")

class Car:
    def drive(self) -> None:
        print("Driving")

# Signature is ignored at runtime — only attribute existence is checked
class Fake:
    def draw(self, x: int, y: int) -> str:
        return "ok"

if __name__ == "__main__":
    print(isinstance(Tree(), Drawable))  # True  – has .draw
    print(isinstance(Car(), Drawable))   # False – no .draw
    print(isinstance(Fake(), Drawable))  # True  – .draw exists (signature ignored)
```

Output:
```
True
False
True
```

> **Limitation:** `@runtime_checkable` only verifies that the method *exists*, not
> its signature. Use it sparingly; protocols are primarily a static analysis tool.


---

## 6. Combining Protocols

Protocols can inherit from other protocols, forming a hierarchy. The derived protocol
requires **all** members from its parents.

```python
# example_proto_combination.py
from typing import Protocol

class Reader(Protocol):
    def read(self) -> str: ...

class Writer(Protocol):
    def write(self, data: str) -> None: ...

class ReadWriter(Reader, Writer, Protocol):
    """Combines reading and writing, and adds flush."""
    def flush(self) -> None: ...

class FileHandler:
    def read(self) -> str:
        return "data from file"
    def write(self, data: str) -> None:
        print(f"Writing: {data}")
    def flush(self) -> None:
        print("Flushed")

def process(rw: ReadWriter) -> None:
    content = rw.read()
    rw.write(content.upper())
    rw.flush()

if __name__ == "__main__":
    process(FileHandler())
```

Output:
```
Writing: DATA FROM FILE
Flushed
```

> Always include `Protocol` in the base classes of a combined protocol (e.g.,
> `class ReadWriter(Reader, Writer, Protocol)`). Omitting it turns the class into a
> regular abstract class.


---

## 7. Generic Protocols

Protocols can be generic using `TypeVar`. This is essential for defining flexible
interfaces like containers, iterators, and transformers.

```python
# example_proto_generic.py
from typing import TypeVar, Protocol

T = TypeVar('T')

class Container(Protocol[T]):
    def __getitem__(self, index: int) -> T: ...
    def __len__(self) -> int: ...

def first_item(cont: Container[T]) -> T:
    return cont[0]

if __name__ == "__main__":
    print(first_item([10, 20, 30]))   # 10
    print(first_item((1.1, 2.2)))     # 1.1
    print(first_item("hello"))        # h
```

Output:
```
10
1.1
h
```

The type variable `T` captures the element type, so the return type of `first_item`
is inferred correctly by the type checker.


---

## 8. Recursive Protocols

Protocols can refer to themselves using a forward reference (string), which is useful
for tree-like structures.

```python
# example_proto_recursive.py
from typing import Protocol, Optional

class TreeNode(Protocol):
    value: int
    left: Optional['TreeNode']
    right: Optional['TreeNode']

class SimpleNode:
    def __init__(self, val: int, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def sum_tree(node: Optional['TreeNode']) -> int:
    if node is None:
        return 0
    return node.value + sum_tree(node.left) + sum_tree(node.right)

if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    root = SimpleNode(1, SimpleNode(2), SimpleNode(3))
    print(sum_tree(root))   # 6
```

Output:
```
6
```


---

## 9. Protocols vs. Abstract Base Classes (ABCs)

| Feature                          | Protocol (structural)                       | ABC (nominal)                          |
|----------------------------------|---------------------------------------------|----------------------------------------|
| Subtyping rule                   | Structural – no inheritance required        | Explicit `class Foo(MyABC)` required   |
| Runtime `isinstance` check       | Only with `@runtime_checkable` (limited)    | Full support                           |
| Default method implementation    | Possible; inherited only by explicit subclasses | Fully supported (mixins)           |
| Static type checking             | Excellent (mypy, pyright)                   | Good, but less flexible                |
| Retroactive typing               | Yes – works on existing classes             | No – must modify or subclass           |
| Best for                         | Flexible interfaces, adapters               | Runtime checks, mixins, frameworks     |

```python
# example_proto_vs_abc.py
from typing import Protocol
from abc import ABC, abstractmethod

# Structural (Protocol) – no inheritance needed
class DrawableProto(Protocol):
    def draw(self) -> None: ...

# Nominal (ABC) – explicit inheritance required
class DrawableABC(ABC):
    @abstractmethod
    def draw(self) -> None: ...

class Picture:               # satisfies DrawableProto structurally
    def draw(self) -> None:
        print("Picture drawn")

class ABCCircle(DrawableABC):  # explicitly subclasses DrawableABC
    def draw(self) -> None:
        print("Circle drawn")

def use_proto(d: DrawableProto) -> None:
    d.draw()

def use_abc(d: DrawableABC) -> None:
    d.draw()

if __name__ == "__main__":
    use_proto(Picture())    # Works – structural match
    use_abc(ABCCircle())    # Works – nominal subclass

    # use_abc(Picture()) would raise TypeError at runtime:
    # Picture is not a subclass of DrawableABC
```

Output:
```
Picture drawn
Circle drawn
```

**When to prefer protocols:** You design an interface for unrelated classes, or you
want to type-check existing libraries without modifying them.

**When to prefer ABCs:** You need reliable runtime `isinstance` checks, concrete
helper methods (mixins), or explicit subclass registration.


---

## 10. Practical Use Cases

### 10.1 Dependency Injection and Testing

Protocols let you declare the *interface* of a dependency without binding to a
concrete class. Swapping in a mock for tests requires no extra setup.

```python
# example_proto_di.py
from typing import Protocol

class EmailSender(Protocol):
    def send(self, to: str, subject: str, body: str) -> bool: ...

class RealMailer:
    def send(self, to: str, subject: str, body: str) -> bool:
        print(f"[REAL] Sending to {to}: {subject}")
        return True

class MockMailer:
    def send(self, to: str, subject: str, body: str) -> bool:
        print(f"[MOCK] Would send to {to}: {subject}")
        return True

def notify_user(sender: EmailSender, email: str) -> None:
    success = sender.send(email, "Welcome", "Thanks for joining!")
    print("Sent" if success else "Failed")

if __name__ == "__main__":
    notify_user(RealMailer(), "alice@example.com")
    notify_user(MockMailer(), "bob@example.com")
```

Output:
```
[REAL] Sending to alice@example.com: Welcome
Sent
[MOCK] Would send to bob@example.com: Welcome
Sent
```

### 10.2 File-like Objects

Instead of requiring a specific `io.IOBase` subclass, define a minimal protocol for
reading. Any object with a `.read()` method qualifies — `open()` files, `BytesIO`,
network streams, custom adapters.

```python
# example_proto_readable.py
from typing import Protocol
from io import BytesIO

class Readable(Protocol):
    def read(self, size: int = -1) -> bytes: ...

def process_data(source: Readable) -> None:
    chunk = source.read(4)
    print(f"First 4 bytes: {chunk}")

if __name__ == "__main__":
    buf = BytesIO(b"Hello, world!")
    process_data(buf)
    # Any custom class with .read(size) works too
```

Output:
```
First 4 bytes: b'Hell'
```

### 10.3 Callable Objects

A protocol with `__call__` describes the signature of a callable more clearly than
the generic `Callable[[int, str], bool]` form.

```python
# example_proto_callable.py
from typing import Protocol

class Filter(Protocol):
    def __call__(self, value: int, mode: str) -> bool: ...

def apply_filter(data: list[int], f: Filter) -> list[int]:
    return [x for x in data if f(x, "strict")]

class GreaterThan:
    def __init__(self, threshold: int):
        self.threshold = threshold
    def __call__(self, value: int, mode: str) -> bool:
        return value > self.threshold

if __name__ == "__main__":
    numbers = [5, 12, 3, 8, 20]
    filtered = apply_filter(numbers, GreaterThan(10))
    print(filtered)   # [12, 20]
```

Output:
```
[12, 20]
```

### 10.4 Repository Pattern

A generic `Repository` protocol decouples business logic from any specific data store
(in-memory, SQLite, REST API, etc.).

```python
# example_proto_repository.py
from typing import Protocol, TypeVar, List, Optional

T = TypeVar('T')

class Repository(Protocol[T]):
    def get(self, id: int) -> Optional[T]: ...
    def save(self, entity: T) -> None: ...
    def list_all(self) -> List[T]: ...

class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}')"

class InMemoryUserRepo:
    def __init__(self):
        self._store: dict[int, User] = {}
    def get(self, id: int) -> Optional[User]:
        return self._store.get(id)
    def save(self, entity: User) -> None:
        self._store[entity.id] = entity
    def list_all(self) -> List[User]:
        return list(self._store.values())

def print_all_users(repo: Repository[User]) -> None:
    for user in repo.list_all():
        print(user)

if __name__ == "__main__":
    repo = InMemoryUserRepo()
    repo.save(User(1, "Alice"))
    repo.save(User(2, "Bob"))
    print_all_users(repo)
    print("Find user 1:", repo.get(1))
    print("Find user 99:", repo.get(99))
```

Output:
```
User(id=1, name='Alice')
User(id=2, name='Bob')
Find user 1: User(id=1, name='Alice')
Find user 99: None
```


---

## 11. Advanced Patterns

### 11.1 `TypeVar` Bound to a Protocol

Bounding a `TypeVar` to a protocol lets a generic function operate on any type that
satisfies the protocol, while preserving the concrete type through the call.

```python
# example_proto_typevar_bound.py
from typing import TypeVar, Protocol

class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool: ...

T = TypeVar('T', bound=Comparable)

def max_of_two(a: T, b: T) -> T:
    return b if a < b else a

class IntWrapper:
    def __init__(self, value: int):
        self.value = value
    def __lt__(self, other: 'IntWrapper') -> bool:
        return self.value < other.value
    def __repr__(self) -> str:
        return f"IntWrapper({self.value})"

if __name__ == "__main__":
    print(max_of_two(IntWrapper(5), IntWrapper(10)))   # IntWrapper(10)
    print(max_of_two(3, 7))                            # 7
    print(max_of_two("apple", "banana"))               # banana
```

Output:
```
IntWrapper(10)
7
banana
```

### 11.2 Self-Type for Fluent Interfaces

Using a `TypeVar` bound to the protocol preserves the concrete return type in
method-chaining (fluent) APIs.

```python
# example_proto_selftype.py
from typing import TypeVar, Protocol

Self = TypeVar('Self', bound='Builder')

class Builder(Protocol):
    def set_name(self: Self, name: str) -> Self: ...
    def set_age(self: Self, age: int) -> Self: ...

class PersonBuilder:
    def __init__(self):
        self.name = ""
        self.age = 0
    def set_name(self, name: str) -> 'PersonBuilder':
        self.name = name
        return self
    def set_age(self, age: int) -> 'PersonBuilder':
        self.age = age
        return self
    def build(self) -> dict:
        return {"name": self.name, "age": self.age}

if __name__ == "__main__":
    result = PersonBuilder().set_name("Alice").set_age(30).build()
    print(result)   # {'name': 'Alice', 'age': 30}
```

Output:
```
{'name': 'Alice', 'age': 30}
```

### 11.3 Async Protocols

Protocols work seamlessly with `async def` methods. Any class with the right async
signature satisfies the protocol.

```python
# example_proto_async.py
import asyncio
from typing import Protocol

class AsyncReader(Protocol):
    async def read(self) -> str: ...

class FileReader:
    async def read(self) -> str:
        await asyncio.sleep(0.01)   # simulates I/O
        return "data from file"

class NetworkReader:
    async def read(self) -> str:
        await asyncio.sleep(0.01)   # simulates network
        return "data from network"

async def consume(reader: AsyncReader) -> None:
    content = await reader.read()
    print(f"Read: {content}")

async def main():
    await consume(FileReader())
    await consume(NetworkReader())

if __name__ == "__main__":
    asyncio.run(main())
```

Output:
```
Read: data from file
Read: data from network
```

### 11.4 Protocols with Class and Static Methods

```python
# example_proto_class_static.py
from typing import Protocol
import json

class Serializable(Protocol):
    @classmethod
    def from_json(cls, data: dict) -> 'Serializable': ...
    def to_json(self) -> dict: ...

class Config:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
    @classmethod
    def from_json(cls, data: dict) -> 'Config':
        return cls(data["host"], data["port"])
    def to_json(self) -> dict:
        return {"host": self.host, "port": self.port}
    def __repr__(self) -> str:
        return f"Config(host='{self.host}', port={self.port})"

def roundtrip(obj: Serializable) -> None:
    serialized = obj.to_json()
    print("Serialized:", json.dumps(serialized))

if __name__ == "__main__":
    cfg = Config("localhost", 8080)
    roundtrip(cfg)
    restored = Config.from_json({"host": "prod.example.com", "port": 443})
    roundtrip(restored)
```

Output:
```
Serialized: {"host": "localhost", "port": 8080}
Serialized: {"host": "prod.example.com", "port": 443}
```


---

## 12. Common Pitfalls

### 12.1 `@runtime_checkable` Does Not Check Attributes

At runtime, `isinstance` only checks that *methods* exist on the object. Attribute
annotations in a protocol are **not** verified.

```python
# example_proto_attribute_gotcha.py
from typing import runtime_checkable, Protocol

@runtime_checkable
class HasName(Protocol):
    name: str   # attribute – NOT checked by isinstance at runtime

class WithoutName:
    pass

class WithName:
    name = "John"

if __name__ == "__main__":
    print(isinstance(WithoutName(), HasName))  # True  – WRONG, has no .name
    print(isinstance(WithName(), HasName))     # True

    # Fix: declare the attribute as a property
    @runtime_checkable
    class FixedHasName(Protocol):
        @property
        def name(self) -> str: ...

    print(isinstance(WithoutName(), FixedHasName))  # False – correctly rejected
    print(isinstance(WithName(), FixedHasName))     # True
```

Output:
```
True
True
False
True
```

### 12.2 Forgetting `Protocol` in Combined Protocols

```python
# Correct – stays a protocol
class ReadWriter(Reader, Writer, Protocol):
    def flush(self) -> None: ...

# Wrong – becomes an ABC, not a protocol
class ReadWriter(Reader, Writer):
    def flush(self) -> None: ...
```

### 12.3 Relying on `@runtime_checkable` for Signature Verification

`isinstance` with a runtime-checkable protocol only checks method *existence*, not
argument types or arity. Do not use it as a substitute for full interface validation.

### 12.4 Python Version Compatibility

`Protocol` requires Python 3.8+. For 3.7, use `typing_extensions.Protocol`.


---

## 13. Best Practices

- **Keep protocols small.** Prefer several focused protocols (`Reader`, `Writer`,
  `Closer`) over one monolithic interface. This follows the Interface Segregation
  Principle.
- **Name protocols clearly.** Adjectives or `-able`/`-er` nouns work well:
  `Comparable`, `Iterable`, `Drawable`, `Serializer`, `Closer`.
- **Use `@runtime_checkable` only when necessary.** Most protocol usage is purely
  static. Delegate verification to a CI-run type checker (`mypy`, `pyright`).
- **Prefer protocols over ABCs for library interfaces** unless you need runtime
  registration, complex mixins, or guaranteed `isinstance` semantics.
- **Document expected behaviour.** A protocol's docstring should explain what each
  method is expected to *do*, not only its signature.
- **Combine with ABC for full runtime + static safety** — define a protocol for
  static checks and a matching ABC for runtime checks. This is rarely needed, but
  available when required.


---

## 14. Summary

| Concept                   | Key point                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| Structural subtyping      | A class matches a protocol if it has the required members, no inheritance needed |
| Defining a protocol       | Subclass `typing.Protocol`; use `...` for method bodies                   |
| Implicit satisfaction     | No `class Foo(MyProtocol)` needed — presence of members is enough         |
| Explicit satisfaction     | Possible and valid; subclass inherits any default implementations         |
| Runtime checking          | Add `@runtime_checkable`; only method existence is verified               |
| Combining protocols       | Inherit multiple protocols + `Protocol`                                   |
| Generic protocols         | Use `Protocol[T]` with a `TypeVar`                                        |
| Recursive protocols       | Forward-reference self with a string: `Optional['TreeNode']`              |
| vs. ABCs                  | Protocols = flexible, static; ABCs = runtime checks, mixins               |

Protocols let you write expressive, decoupled, and statically verifiable Python code
while fully honouring the dynamic spirit of duck typing. Start with small,
single-purpose protocols and compose them as your design grows.
