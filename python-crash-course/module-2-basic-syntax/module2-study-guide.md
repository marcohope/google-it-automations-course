# Module 2 — Basic Python Syntax: Study Guide

---

## 1. Expressions & Variables

### Data Types

| Type | Example | Notes |
|---|---|---|
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"hello"` | Text in quotes |
| `bool` | `True` / `False` | Capitalized |
| `None` | `None` | Absence of value |

### Type Conversion

**Implicit** — Python handles it automatically:

```python
print(7 + 5.5)  # 12.5 (int + float → float)
```

**Explicit** — you convert manually:

```python
str(42)      # "42"
int("10")    # 10
float("3.5") # 3.5
```

Example:

```python
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is " + str(average))
```

### Operators

| Operator | Meaning |
|---|---|
| `+` `-` `*` `/` | Basic arithmetic |
| `**` | Exponent |
| `%` | Modulo (remainder) |
| `//` | Floor division |

---

## 2. Variable Naming

### Hard Rules (code breaks if violated)

| Rule | Valid | Invalid |
|---|---|---|
| Must start with letter or `_` | `name`, `_var` | `2var`, `@var` |
| Only letters, digits, underscores | `user_name` | `user-name`, `user name` |
| Case-sensitive | `name` ≠ `Name` | — |
| Cannot be a Python keyword | `user` | `if`, `for`, `class` |

### Naming Conventions (PEP 8)

| Context | Style | Example |
|---|---|---|
| Variables & functions | `snake_case` | `user_name`, `get_total()` |
| Constants | `UPPER_CASE` | `MAX_RETRIES`, `PI` |
| Classes | `PascalCase` | `UserAccount` |

> Use descriptive names — `student_name` is better than `sn`.

### Type Annotations (optional but helpful)

```python
name: str = "Betty"
age: int = 34
```

---

## 3. Functions

### Defining a Function

```python
def function_name(parameter1, parameter2):
    # body
    return result
```

### Example

```python
def grade(name, score):
    print(name + " scored " + str(score))

grade("Marco", 99)  # Marco scored 99
```

### Returning Values

```python
def area_triangle(base, height):
    return 0.5 * base * height

area_a = area_triangle(10, 5)  # 25.0
area_b = area_triangle(7, 3)   # 10.5
print("Total area: " + str(area_a + area_b))
```

> A function without `return` implicitly returns `None`.

### Multiple Return Values

```python
def converting_seconds(seconds):
    hours   = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    secs    = seconds - hours * 3600 - minutes * 60
    return hours, minutes, secs

hours, minutes, seconds = converting_seconds(5000)
print(hours, minutes, seconds)  # 1 23 20
```

### Code Reuse — Why Functions Matter

Without a function (repeated logic):

```python
name = "Kay"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))
```

With a function:

```python
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")
```

### Built-in Functions

| Function | Description | Example |
|---|---|---|
| `print()` | Outputs to screen | `print("hello")` |
| `type()` | Returns type of a value | `type(42)` → `<class 'int'>` |
| `len()` | Length of a string/list | `len("hello")` → `5` |
| `str()` | Converts to string | `str(42)` → `"42"` |
| `int()` | Converts to integer | `int("5")` → `5` |
| `float()` | Converts to float | `float("3.14")` → `3.14` |
| `sorted()` | Returns sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `min()` | Smallest value | `min([3,1,2])` → `1` |
| `max()` | Largest value | `max([3,1,2])` → `3` |

---

## 4. Conditionals

### Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `1 == 1` → `True` |
| `!=` | Not equal to | `1 != 2` → `True` |
| `>` | Greater than | `10 > 1` → `True` |
| `<` | Less than | `1 < 10` → `True` |
| `>=` | Greater than or equal | `5 >= 5` → `True` |
| `<=` | Less than or equal | `3 <= 4` → `True` |

> Comparing incompatible types (e.g. `1 < "1"`) raises a `TypeError`.

### Logical Operators

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both must be True | `True and False` → `False` |
| `or` | At least one True | `True or False` → `True` |
| `not` | Inverts the value | `not True` → `False` |

```python
print("Yellow" > "Cyan" and "Brown" > "Magenta")  # False
print(25 > 50 or 1 != 2)                          # True
print(not 42 == "Answer")                          # True
```

### `if` / `elif` / `else`

```python
number = -4

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")
```

### Practical Example — Username Validation

```python
def hint_username(username):
    if len(username) < 3:
        print("Too short — must be at least 3 characters")
    elif len(username) > 15:
        print("Too long — must be at most 15 characters")
    else:
        print("Valid username")
```

### Returning a Boolean

```python
def is_even(number):
    if number % 2 == 0:
        return True
    return False
```

---

## Key Concepts Checklist

- [ ] Convert between `int`, `float`, and `str`
- [ ] Name variables using `snake_case`
- [ ] Define functions with `def` and call them
- [ ] Use `return` to pass values back from a function
- [ ] Unpack multiple return values
- [ ] Use `if` / `elif` / `else` to branch logic
- [ ] Use comparison and logical operators correctly
- [ ] Use built-in functions: `len()`, `type()`, `sorted()`, `min()`, `max()`
