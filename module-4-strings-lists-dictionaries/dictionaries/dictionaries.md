# Dictionaries — Study Guide

A quick-reference summary of Python dictionaries: what they are, how to use them, and common operations.

---

## What is a Dictionary?

A **dictionary** is a collection of **key-value pairs**. Unlike lists (which are indexed by position), dictionaries are indexed by **keys**.

- **Keys** must be unique and **immutable** (strings, numbers, tuples — never lists).
- **Values** can be any type (strings, numbers, lists, even other dictionaries).
- Dictionaries are **mutable** — you can add, change, or remove items.
- As of Python 3.7+, dictionaries preserve **insertion order**.

```python
# Empty dictionary
empty = {}

# Dictionary with initial values
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
```

---

## Common Dictionary Operations

| Operation | Description |
|---|---|
| `len(dict)` | Returns the number of key-value pairs |
| `dict[key]` | Returns the value associated with `key` (raises `KeyError` if missing) |
| `dict[key] = value` | Adds a new pair or updates an existing key's value |
| `del dict[key]` | Removes the key-value pair |
| `key in dict` | Returns `True` if `key` exists in the dictionary |
| `for key in dict` | Iterates over keys |
| `for key, value in dict.items()` | Iterates over keys and values simultaneously |

---

## Dictionary Methods

| Method | Description |
|---|---|
| `dict.get(key, default)` | Returns value for `key`; returns `default` (or `None`) if key not found |
| `dict.keys()` | Returns a view of all keys |
| `dict.values()` | Returns a view of all values |
| `dict.items()` | Returns a view of (key, value) tuples |
| `dict.pop(key)` | Removes and returns the value for `key` |
| `dict.update(other_dict)` | Merges `other_dict` into the dictionary |
| `dict.clear()` | Removes all items |
| `dict.copy()` | Returns a shallow copy |

---

## Accessing Values

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

print(file_counts["jpg"])          # 10
print(file_counts.get("png"))      # None (no error)
print(file_counts.get("png", 0))   # 0 (default value)
```

> Use `.get()` when you're not sure if a key exists — it avoids `KeyError`.

---

## Adding, Updating, and Removing

```python
file_counts = {"jpg": 10, "txt": 14}

# Add a new pair
file_counts["py"] = 23

# Update an existing value
file_counts["jpg"] = 15

# Remove a pair
del file_counts["txt"]

print(file_counts)  # {"jpg": 15, "py": 23}
```

---

## Checking for Keys

```python
file_counts = {"jpg": 10, "txt": 14}

if "jpg" in file_counts:
    print("Found jpg files")

if "png" not in file_counts:
    print("No png files")
```

---

## Iterating Through a Dictionary

### Iterate over keys (default)

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2}

for extension in file_counts:
    print(extension)
# jpg
# txt
# csv
```

### Iterate over keys and values with `.items()`

```python
for extension, count in file_counts.items():
    print(f"There are {count} {extension} files")
# There are 10 jpg files
# There are 14 txt files
# There are 2 csv files
```

### Iterate over just values

```python
for count in file_counts.values():
    print(count)
```

---

## Dictionary Comprehensions

Like list comprehensions, but for dictionaries.

```python
# Square each number
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter while building
file_counts = {"jpg": 10, "txt": 14, "csv": 2}
big_groups = {ext: n for ext, n in file_counts.items() if n > 5}
print(big_groups)  # {"jpg": 10, "txt": 14}
```

---

## Lists vs. Dictionaries

| Feature | List | Dictionary |
|---|---|---|
| Access by | Index (position) | Key |
| Order | Ordered | Insertion-ordered (3.7+) |
| Duplicates | Allowed | Keys must be unique |
| Best for | Sequences of items | Lookups, mappings, counts |
| Mutable? | Yes | Yes |

---

## Common Patterns

### Counting occurrences

```python
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("apple"))
# {'a': 1, 'p': 2, 'l': 1, 'e': 1}
```

### Inverting a dictionary (swap keys and values)

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Grouping items

```python
def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

print(group_by_length(["hi", "bye", "yes", "hello"]))
# {2: ['hi'], 3: ['bye', 'yes'], 5: ['hello']}
```

### Merging dictionaries

```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

a.update(b)
print(a)  # {"x": 1, "y": 99, "z": 3}

# Or with the merge operator (Python 3.9+):
merged = a | b
```

---

## Gotchas

- **Keys must be immutable.** You can use strings, numbers, or tuples — but not lists.
  ```python
  bad = {[1, 2]: "value"}    # TypeError: unhashable type: 'list'
  good = {(1, 2): "value"}   # works
  ```
- **`dict[missing_key]` raises `KeyError`.** Use `.get()` or check with `in` first.
- **Modifying a dictionary while iterating** can cause errors — iterate over a copy of the keys if you need to delete items.
  ```python
  for key in list(my_dict.keys()):
      if some_condition:
          del my_dict[key]
  ```

---

## Resources

- [Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) — python.org docs for dictionary operations and methods
- [Dictionary view objects](https://docs.python.org/3/library/stdtypes.html#dict-views) — `.keys()`, `.values()`, `.items()`
