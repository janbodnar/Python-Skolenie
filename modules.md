# Python Modules 

A **module** is a Python file containing definitions, statements, and optionally executable code.  
By grouping related functions, classes, and variables into modules, you transform sprawling scripts  
into maintainable, reusable, and testable components.

Python organizes code hierarchically:
- **Functions** → atomic units of behavior
- **Classes** → encapsulate state and methods
- **Modules** → individual `.py` files
- **Packages** → directories containing modules, forming a structured namespace

When a script exceeds a few dozen lines, splitting it into modules becomes essential. For instance,  
database interactions belong in a `db.py` module, authentication logic in `auth.py`, and configuration  
parsing in `config.py`. Related modules are grouped into **packages** to create a clean, scalable architecture.


## 1. Module Names and the `__name__` Variable

Every module carries a unique name. For a file named `empty.py`, the module name is `empty`.  
Python automatically sets the special variable `__name__` to the module's name. When you run  
a file directly as a script, Python assigns `__name__` the value `'__main__'`.

**empty.py**
```python
"""An intentionally minimal module."""
```

**test_empty.py**
```python
import empty
import sys

print(__name__)        # __main__
print(empty.__name__)  # empty
print(sys.__name__)    # sys
```

Running the script:
```bash
$ python test_empty.py
__main__
empty
sys
```

This dual-identity mechanism enables a single file to act as both a reusable library  
and a standalone script. The `if __name__ == '__main__':` idiom (covered later)  
leverages this behavior.


## 2. How Python Finds Modules

When you execute `import mymodule`, Python follows a deterministic search order:

1. **Built-in modules** (compiled into the interpreter, e.g., `sys`, `math`)
2. **`sys.modules` cache** (prevents re-importing and speeds up execution)
3. **File system search** via `sys.path`

`sys.path` is a list of directory strings assembled from:
- The directory containing the entry script (or `''` for interactive mode, meaning the current working directory)
- Directories specified in the `PYTHONPATH` environment variable
- Installation-specific paths (e.g., `site-packages` managed by `pip` or `venv`)

You can inspect your search path:
```python
import sys
import textwrap

print(textwrap.fill(', '.join(sys.path), width=80))
```

**Sample output:**
```
/home/user/project, /usr/lib/python310.zip, /usr/lib/python3.10, 
/usr/lib/python3.10/lib-dynload, /home/user/.local/lib/python3.10/site-packages, 
/usr/lib/python3/dist-packages
```

⚠️ While you can modify `sys.path` at runtime (`sys.path.insert(0, '/custom/lib')`), it's generally discouraged. Prefer virtual environments, `PYTHONPATH`, or proper packaging (`pyproject.toml` + `pip install -e .`) for predictable dependency resolution.

If a module isn't found, Python raises `ModuleNotFoundError` (a subclass of `ImportError`, introduced in Python 3.6).

---

## 3. Name Clashes: The Shadowing Problem

A common beginner mistake is naming a script after a standard library or third-party package. If you create `requests.py` in your project root, `import requests` will load *your file* instead of the actual `requests` library, because the script's directory appears first in `sys.path`.

**Example of accidental shadowing:**
```python
# File: json.py (don't do this!)
import json  # Imports itself! Raises AttributeError on json.loads()

data = '{"name": "Alice"}'
print(json.loads(data))  # Fails: module has no attribute 'loads'
```

**How to avoid it:**
- Never reuse names of built-in or popular third-party modules.
- Use linters (`flake8`, `pylint`, `ruff`) which flag shadowed imports automatically.
- Verify imports in a clean REPL before committing code.

---

## 4. Import Styles & PEP 8 Guidelines

Python provides flexible import syntax. Choosing the right style improves readability and prevents namespace pollution.

| Style | Syntax | When to Use |
|-------|--------|-------------|
| **Full module import** | `import math` | Preferred. Explicit, avoids collisions, self-documenting. |
| **Selective import** | `from math import pi, sin` | When using only a few names repeatedly. |
| **Aliased import** | `import numpy as np` | For long names or resolving conflicts. |
| **Wildcard import** | `from math import *` | **Discouraged**. Only for interactive exploration. |

**Multiline imports** (PEP 8 compliant):
```python
from datetime import (
    datetime,
    timedelta,
    timezone
)
```

**Aliasing for readability:**
```python
from very.long.package.name.utils import helper as util_helper
```

---

## 5. Wildcard Imports & Namespace Pollution

Wildcard imports (`from module import *`) inject all public names into the current namespace. This can silently overwrite variables, confuse readers, and break static analyzers.

**Example of shadowing:**
```python
from math import *
pi = 3.14  # Overwrites math.pi
print(cos(0))  # Works
print(pi)      # 3.14, not 3.1415926535...
```

In large codebases, this leads to subtle, hard-to-debug bugs. PEP 8 explicitly recommends against `*` imports outside of interactive sessions or very controlled internal modules.

---

## 6. Private Names & Controlling Exports with `__all__`

Python uses naming conventions to signal visibility:
- `_single_leading_underscore`: Internal/private. Excluded from `import *`.
- `__double_leading_underscore`: Triggers name mangling in classes (not relevant to module imports).

You can override the default `*` behavior by defining `__all__`, a list of public identifiers:

**`mymodule.py`**
```python
__all__ = ["process_data", "VERSION"]

def process_data(data: list) -> list:
    return sorted(data)

def _validate(data: list) -> bool:
    return all(isinstance(x, (int, float)) for x in data)

VERSION = "2.1.0"
```

Now, `from mymodule import *` only exposes `process_data` and `VERSION`. Users can still explicitly import `_validate`, but doing so signals they're relying on internal implementation details that may change without notice.

---

## 7. Handling Import Errors Gracefully

Missing modules don't have to crash your application. Use `try/except` for optional dependencies or fallback behavior:

```python
try:
    import orjson as json
except ImportError:
    import json  # Fallback to standard library

print(json.dumps({"status": "ok"}))
```

**Checking installation without importing:**
```python
import importlib.util
import sys

if importlib.util.find_spec("pandas") is not None:
    print("pandas is installed")
else:
    print("pandas missing. Install with: pip install pandas")
```

This pattern is widely used in libraries that support multiple backends (e.g., `pydantic`, `httpx`).

---

## 8. The `__main__` Guard & Dual-Purpose Modules

Modules often need to run standalone for testing or CLI usage. The `if __name__ == '__main__':` block ensures code inside it only executes when the file is the entry point.

**`fibonacci.py`**
```python
"""Calculate Fibonacci numbers up to n."""

def fib_sequence(limit: int) -> list[int]:
    seq = []
    a, b = 0, 1
    while a < limit:
        seq.append(a)
        a, b = b, a + b
    return seq

if __name__ == "__main__":
    import sys
    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        n = 100
    print(f"Fibonacci up to {n}:", fib_sequence(n))
```

Run as script:

```bash
$ python fibonacci.py 50
Fibonacci up to 50: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

Import as library:

```python
import fibonacci
print(fibonacci.fib_sequence(30))
```

You can also execute modules directly using `python -m package.module`, which preserves  
relative imports and package context.


## 9. Introspection: `dir()`, `globals()`, and `vars()`

| Function | Returns | Typical Use |
|----------|---------|-------------|
| `dir(obj)` | Sorted list of attributes/names | Debugging, exploring APIs |
| `globals()` | Dict of current module's global namespace | Dynamic lookup, metaprogramming |
| `vars(obj)` | Dict of an object's `__dict__` | Inspecting instance/state attributes |

**Example:**
```python
import math

PI_APPROX = 3.14
names = ["Alice", "Bob"]

print(dir())  # Includes '__builtins__', 'math', 'PI_APPROX', 'names', ...
print(globals()['PI_APPROX'])  # 3.14
```

Avoid mutating `globals()` directly. It breaks static analysis, complicates debugging,  
and often indicates a design flaw. Prefer dictionaries or configuration objects for dynamic state.


## 10. The `__module__` Attribute

Classes, functions, and methods store their origin module in `__module__`. This is invaluable  
for serialization, logging, and framework development.

**`animals.py`**
```python
class Cat:
    pass

class Dog:
    pass
```

**`main.py`**
```python
from animals import Cat

class Being:
    pass

b = Being()
c = Cat()

print(b.__module__)  # __main__
print(c.__module__)  # animals
print(Cat.__module__)  # animals
```

Frameworks like `pydantic`, `sqlalchemy`, and `logging` use `__module__` to resolve types,  
generate documentation, or route events correctly.


## 11. Bytecode Caching (`.pyc` Files)

To speed up subsequent imports, Python compiles source files into bytecode and caches  
them in `__pycache__/`. Files are named like `module.cpython-310.pyc`, embedding the  
interpreter version.

Python automatically:

- Recompiles if the `.py` file is newer than the `.pyc`
- Skips caching if the directory isn't writable
- Ignores stale caches if versions mismatch

**View bytecode:**
```python
import dis
dis.dis("def add(a, b): return a + b")
```

**Control caching:**
```bash
# Skip writing .pyc files
python -B script.py
export PYTHONDONTWRITEBYTECODE=1

# Compile an entire directory
python -m compileall lib/
```

🚫 Never commit `__pycache__/` to version control. Add it to `.gitignore`.

---

## 12. Packages: Regular vs. Namespace

A **package** is a directory containing Python modules. Python supports two package types:

### Regular Packages
Require an `__init__.py` file (can be empty). Executed once on first import. Often used to re-export APIs:

```
mylib/
    __init__.py
    core.py
    utils.py
```

**`__init__.py`**
```python
from .core import Engine
from .utils import configure

__all__ = ["Engine", "configure"]
```

Now users can simply do: `from mylib import Engine`

### Namespace Packages (PEP 420)

If a directory lacks `__init__.py`, Python treats it as a **namespace package**. Multiple directories  
across `sys.path` can contribute to the same top-level name. Widely used by large ecosystems  
(e.g., `google.cloud.*`, `azure.*`) to split code across separate distributions.

---

## 13. Relative Imports & Common Pitfalls

Inside packages, use relative imports to reference siblings:

```
project/
    pkg/
        __init__.py
        models.py
        services/
            __init__.py
            auth.py
            db.py
```

**`services/db.py`**
```python
from ..models import User      # Parent package
from . import auth             # Sibling module
from .auth import verify_token # Explicit submodule
```

**Crucial Rule:** Relative imports only work when the module is executed as part of   
a package (`python -m pkg.services.db`). Running `db.py` directly raises:

```
ImportError: attempted relative import with no known parent package
```

**Fix:** Always run packaged code with `python -m`, or use absolute imports (`from project.pkg.models import User`) for top-level scripts.

---

## 14. Dynamic Imports with `importlib`

When module names are determined at runtime (plugins, config-driven systems), use `importlib`:

```python
import importlib

module_name = "math"
mod = importlib.import_module(module_name)
print(mod.sqrt(25))  # 5.0
```

**Loading a module from an arbitrary file path:**
```python
import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location(
    "dynamic_module", pathlib.Path("/tmp/plugins/loader.py")
)
dynamic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic)

dynamic.run()
```

This pattern powers plugin architectures, test runners, and hot-reload systems.

---

## 15. Modern Best Practices

| Practice | Why It Matters |
|----------|----------------|
| **Use `src/` layout** | Prevents accidental imports of local files during testing. |
| **Define `__all__`** | Creates a stable public API; hides internals. |
| **Avoid circular imports** | Break with interfaces, lazy imports inside functions, or dependency injection. |
| **Prefer absolute imports in apps** | Clearer navigation, IDE-friendly, avoids relative import confusion. |
| **Use `pyproject.toml` + `pip install -e .`** | Modern packaging standard; handles dependencies and editable installs cleanly. |
| **Add type hints** | Improves static analysis, autocomplete, and documentation. |
| **Never modify `sys.path` in production** | Use virtual environments or proper packaging instead. |

**Avoiding circular imports example:**
```python
# ❌ BAD: a.py imports b.py, b.py imports a.py
# ✅ GOOD: Extract shared interface to c.py, or import inside functions
def process():
    from .other_module import heavy_function  # Lazy import
    return heavy_function()
```

## Conclusion

Modules and packages are the architectural foundation of Python projects. Mastering the import system,  
understanding `__name__`, leveraging `__all__`, and respecting package boundaries transforms fragile  
scripts into robust, scalable applications.

From single-file utilities to enterprise-grade systems, Python's modular design scales effortlessly when  
you follow explicit, predictable import patterns. Combine these practices with modern tooling  
(`ruff`, `mypy`, `pyproject.toml`, `pytest`) and your codebase will remain clean, testable,  
and maintainable for years to come.
