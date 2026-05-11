# Lists & Tuples — Study Guide

This study guide provides a quick-reference summary of what you learned in this lesson and serves as a guide for the upcoming practice quiz.

---

## Common Sequence Operations

Lists and tuples are both **sequences** and share the following operations:

| Operation | Description |
|---|---|
| `len(sequence)` | Returns the length of the sequence |
| `for element in sequence` | Iterates over each element |
| `if element in sequence` | Checks if element is in the sequence |
| `sequence[x]` | Accesses element at index `x` (zero-based) |
| `sequence[x:y]` | Slice from index `x` up to (not including) `y` |
| `for index, element in enumerate(sequence)` | Iterates over indices and elements simultaneously |

> **Note:** Integers are not iterable — convert to a range first:
> ```python
> for x in range(len(someList)):
>     print(x)
> ```

---

## List-Specific Operations & Methods

Lists are **mutable** (changeable); tuples are **immutable** (not changeable).

| Operation / Method | Description |
|---|---|
| `list[index] = x` | Replaces element at `index` with `x` |
| `list.append(x)` | Appends `x` to the end |
| `list.insert(index, x)` | Inserts `x` at position `index` |
| `list.pop(index)` | Returns and removes element at `index` (last element if omitted) |
| `list.remove(x)` | Removes the first occurrence of `x` |
| `list.sort()` | Sorts items in place |
| `list.reverse()` | Reverses the order of items in place |
| `list.clear()` | Deletes all items |
| `list.copy()` | Returns a shallow copy of the list |
| `list.extend(other_list)` | Appends all elements of `other_list` to the end |
| `map(function, iterable)` | Applies a function to each item; returns a map object |
| `zip(*iterables)` | Combines iterables into an iterator of tuples |

---

## Tuple Use Cases

| Use Case | Why Tuples? |
|---|---|
| **Protecting data** | Immutable — data cannot be accidentally modified |
| **Hashable keys** | Can be used as dictionary keys (lists cannot) |
| **Efficiency** | More memory-efficient than lists for large datasets |

### The `tuple()` Operator

Converts any iterable (list, string, set) into a tuple:

```python
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 4)

# Parentheses are optional when defining a tuple
my_tuple = 1, 2, 3, 4
print(my_tuple)  # (1, 2, 3, 4)
```

### Tuples with Mutable Objects

A tuple is immutable, but it can *contain* mutable objects (like lists):

```python
my_tuple = (1, 2, ['a', 'b', 'c'])
# my_tuple[0] = 3  # TypeError — can't modify the tuple itself
my_tuple[2][0] = 'x'
print(my_tuple)  # (1, 2, ['x', 'b', 'c'])
```

### Returning Multiple Values from Functions

Tuples allow a function to return more than one result:

```python
def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

result = calculate_numbers(10, 2)
print(result)  # (12, 8, 20, 5.0)

# Unpack into separate variables
add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # 12
```

---

## List Comprehensions

A concise way to build a new list from a sequence or range in one line.

| Syntax | Description |
|---|---|
| `[expression for variable in sequence]` | New list from every element |
| `[expression for variable in sequence if condition]` | New list filtered by condition |

```python
# Squares of 1–10
my_list = [x*2 for x in range(1, 11)]

# Multiples of 10 up to 100
my_list = [x for x in range(1, 101) if x % 10 == 0]

# Tuples don't have comprehensions, but this works:
my_tuple = tuple(i for i in (1, 2, 3))
```

### `for` Loop vs. List Comprehension

| Use | When |
|---|---|
| **List comprehension** | Simple transformations or filtering, single-expression result |
| **`for` loop** | Complex logic, multiple lines, `print`/`pass`/`break`/`continue`, no new list needed |

---

## Coding Skills Reference

### Skill 1 — `for` loop + `list.append()` + string methods

```python
years = ["January 2023", "May 2025", "April 2023", "August 2024"]
updated_years = []

for year in years:
    if year.endswith("2023"):
        new = year.replace("2023", "2024")
        updated_years.append(new)
    else:
        updated_years.append(year)

print(updated_years)
# ["January 2024", "May 2025", "April 2024", "August 2024"]
```

### Skill 2 — List comprehension returning values

```python
def squares(start, end):
    return [n*n for n in range(start, end+1)]

print(squares(1, 5))   # [1, 4, 9, 16, 25]
print(squares(0, 10))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Skill 3 — List comprehension with conditional expression

```python
years = ["January 2023", "May 2025", "April 2023", "August 2024"]
updated_years = [
    year.replace("2023", "2024") if year[-4:] == "2023" else year
    for year in years
]
```

### Skill 4 — `string.split()`, index slicing, `+=` concatenation

```python
def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
    return new_string

print(change_string("1one 2two 3three"))  # "one-1 two-2 three-3 "
```

### Skill 5 — `string.join()`

```python
def list_elements(list_name, elements):
    return "The " + list_name + " list includes: " + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "B&W Printer", "3-D Printer"]))
# "The Printers list includes: Color Printer, B&W Printer, 3-D Printer"
```

### Skill 6 — `map()`

```python
def add_one(number):
    return number + 1

numbers = [1, 2, 3, 4, 5]
result = map(add_one, numbers)
print(list(result))  # [2, 3, 4, 5, 6]
```

### Skill 7 — `zip()`

```python
names = ["Alice", "Bob", "Charlie"]
ages  = [25, 30, 35]

combined = zip(names, ages)
print(list(combined))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

---

## Resources

- [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) — python.org docs for list, tuple, and range operations
- [Lists](https://docs.python.org/3/library/stdtypes.html#lists) — python.org docs for list operations and methods
- [Tuples](https://docs.python.org/3/library/stdtypes.html#tuples) — python.org docs for tuple operations and methods
