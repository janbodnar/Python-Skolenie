# Python Code Quality Tools

Writing correct Python is only half the job — keeping it readable and free of
silent bugs is the other half. This guide covers the two main categories of
tools that help with that: **formatters**, which reformat your code to a
consistent style, and **linters**, which analyze your code for errors and
style violations. It also covers `Ruff`, a modern tool that does both, and
shows how to wire everything into VS Code.

## Formatters

A formatter automatically rewrites your code to follow a consistent style —
indentation, spacing, line length, quote style, and so on. You stop thinking
about formatting and start relying on the tool to handle it.

**Example:** Black turns inconsistent spacing and quoting into a single,
predictable style automatically.

Before:
```python
def add(a,b):
    return a+b
x = { 'a':1,'b':2 }
```

After running `black`:
```python
def add(a, b):
    return a + b


x = {"a": 1, "b": 2}
```

Common formatters:

| Tool | Notes |
|------|-------|
| `black` | Opinionated — almost no configuration, one consistent style |
| `autopep8` | Follows PEP 8; more configurable than Black |
| `yapf` | Highly configurable formatting rules |
| `isort` | Formats and groups only your `import` statements |

Install and run Black:
```bash
pip install black
black my_script.py        # reformat a file
black .                    # reformat everything in the current directory
```

## Linters

A linter analyzes your code without running it (static analysis) and flags
problems — think of it as a spell-checker for code. It typically catches:

- **Syntax errors** — code that won't run at all
- **Style violations** — inconsistent naming, indentation, unused imports
- **Likely bugs** — logic issues that formatters can't detect, like an
  undefined variable or a comparison that's always false

Common linters:

| Tool | Notes |
|------|-------|
| `pylint` | Deep analysis, many configurable checks |
| `flake8` | Combines pycodestyle + pyflakes; a common default choice |
| `mypy` | Not a general linter — checks type hints for consistency |

Install and run Flake8:
```bash
pip install flake8
flake8 my_script.py
```

Example output:
```
my_script.py:3:1: F841 local variable 'x' is assigned to but never used
my_script.py:5:80: E501 line too long (92 > 79 characters)
```

Linters are most useful wired into your editor, so problems are flagged as
you type rather than after you run the tool manually.

## Ruff: formatter and linter in one

`Ruff` is a modern tool written in Rust that combines linting and formatting
in a single, very fast binary — commonly used as a drop-in replacement for
Flake8, Pylint, Black, and isort together.

Key points:

- **Fast** — typically 10–100x faster than the tools it replaces, which
  matters on large codebases or in CI
- **One tool, two jobs** — lints and formats without needing separate
  packages
- **700+ built-in rules**, covering style, correctness, and common bug
  patterns, most with automatic fixes
- **Single config file** — one `pyproject.toml` section instead of separate
  configs for Flake8, Black, and isort

Install and run Ruff:
```bash
pip install ruff
ruff check .        # lint
ruff check --fix .  # lint and auto-fix what it can
ruff format .       # format
```

For most new projects, Ruff alone covers what Flake8 + Black + isort used to
require separately.

## Editor Integration: VS Code

The settings below go in your workspace or user `settings.json`. The ones
that actually matter for Python are the formatter binding and the line
ruler; the rest are general editor preferences included here for
convenience — adjust freely to your own taste.

```json
{
    // Python-specific: sets the formatter and runs it on save
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true
    },
    // Visual guide at PEP 8's 79/80-character line length
    "editor.rulers": [80],

    // General editor preferences
    "editor.minimap.enabled": true,
    "editor.renderWhitespace": "all",
    "editor.fontFamily": "Cascadia Code NF, Consolas, 'Courier New', monospace",
    "editor.fontSize": 14,
    "editor.stickyScroll.enabled": false,
    "workbench.editor.enablePreview": true,
    "explorer.autoReveal": true
}
```

Install the **Ruff** extension (`charliermarsh.ruff`) from the VS Code
marketplace to get linting, formatting, and auto-fix-on-save without
installing separate extensions for Black, Flake8, and isort.

## Summary

| Need | Tool |
|------|------|
| Just formatting | `black` |
| Just linting | `flake8` or `pylint` |
| Type checking | `mypy` |
| Both, fast, one config | `ruff` |
