# Module 1 — Hello Python: Study Guide

---

## What is Python?

Python is a general-purpose, high-level programming language used for automation, data science, web development, and more. It reads like plain English and uses **indentation** (not curly braces) to define code blocks.

---

## Your First Program

```python
print("Hello, World!")
```

`print()` outputs text to the screen. Strings can use single `'` or double `"` quotes — they must match.

```python
name = "Brook"
print("Hello " + name)  # Hello Brook
```

---

## Variables

A variable is a name that stores a value.

```python
name = "Brook"   # str
age  = 25        # int
pi   = 3.14      # float
```

- Variables are assigned with `=`
- Python is **dynamically typed** — the type is set by the value, not declared

---

## Data Types (Quick Reference)

| Type | Example | Notes |
|---|---|---|
| `int` | `42`, `-10` | Whole numbers |
| `float` | `3.14`, `-2.5` | Decimal numbers |
| `str` | `"hello"` | Text, in quotes |
| `bool` | `True`, `False` | Capitalized |
| `NoneType` | `None` | Absence of value |
| `list` | `[1, 2, 3]` | Ordered, mutable |
| `tuple` | `(1, 2, 3)` | Ordered, immutable |
| `dict` | `{"key": "val"}` | Key-value pairs |

Check the type of any value with `type()`:

```python
print(type(42))      # <class 'int'>
print(type("hello")) # <class 'str'>
```

---

## Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `4 + 5` | `9` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `3 * 4` | `12` |
| `/` | Division | `10 / 4` | `2.5` |
| `**` | Exponent | `2 ** 10` | `1024` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |

---

## String Concatenation

Join strings with `+`:

```python
name = "Brook"
print("Hello " + name)  # Hello Brook
```

> You cannot concatenate a string and a number directly — use `str()` to convert first:

```python
age = 25
print("Age: " + str(age))  # Age: 25
```

---

## The `math` Module

```python
import math

print(math.sqrt(16))  # 4.0
print(2 ** 10)        # 1024
```

---

## Basic `for` Loop

```python
for i in range(10):
    print("Hello, world!")  # Prints 10 times
```

Iterating over a list:

```python
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
```

`range(n)` generates numbers from `0` up to (not including) `n`.

---

## Key Concepts Checklist

- [ ] Run a Python script
- [ ] Use `print()` to display output
- [ ] Assign and use variables
- [ ] Identify data types with `type()`
- [ ] Perform arithmetic operations
- [ ] Concatenate strings with `+`
- [ ] Convert types with `str()`, `int()`, `float()`
- [ ] Write a basic `for` loop with `range()`
- [ ] Import and use the `math` module
