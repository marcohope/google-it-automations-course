# Python Data Structures Comparison

A reference guide comparing Python's core data structures: **Dictionary**, **Set**, **List**, **String**, and **Tuple**.

---

## Quick Comparison Table

| Feature | Dictionary | Set | List | String | Tuple |
|---|---|---|---|---|---|
| **Definition** | Stores `key: value` pairs | An unordered collection of unique elements | A sequential, mutable collection of any data type | A sequential, immutable collection of textual data | A sequential, immutable collection of any data type |
| **Representation** | `{'a': [42], 'b': [23, 6, 1]}` | `{'^2', 'mc', 'equal', 'E'}` | `['a', 'b', 3, 4]` | `"call me ishmael"` | `('commander', 'lambda')` |
| **How to create** | `x = {}` or `x = dict()` | `x = set()` | `x = []` or `x = list()` | `x = ""` or `x = str()` | `x = ('a', 'b',)` or `x = tuple()` |
| **Mutable / Duplicates** | Immutable keys, mutable values; duplicate values allowed | Mutable, unique elements only | Mutable, duplicates allowed | Immutable, duplicates allowed | Immutable, duplicates allowed |
| **Iterable / Ordered** | Iterable but unordered (insertion order preserved in Python 3.7+) | Iterable but unordered | Iterable, supports numeric indexing | Iterable, sequence of characters | Iterable, supports numeric indexing |

---

## Dictionary

### Definition
Stores data as `key: value` pairs. Keys must be unique and immutable (strings, numbers, tuples). Values can be any type.

### How It's Used
- Counting occurrences of items
- Mapping one thing to another (e.g., username → email)
- Storing structured records (like JSON-style data)
- Fast lookups by key

### Examples
```python
# Creating a dictionary
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

# Accessing a value by key
print(file_counts["txt"])           # 14

# Checking if a key exists
print("jpg" in file_counts)         # True

# Adding or updating a key
file_counts["xml"] = 8              # adds new key
file_counts["csv"] = 13             # overrides existing

# Deleting a key
del file_counts["py"]

# Iterating
for extension, count in file_counts.items():
    print(extension, count)
```

---

## Set

### Definition
An unordered collection of unique, immutable elements. Sets automatically remove duplicates.

### How It's Used
- Removing duplicates from a list
- Membership testing (is X in this group?)
- Mathematical operations: union, intersection, difference

### Examples
```python
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Removing duplicates from a list
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)               # {1, 2, 3}

# Adding and removing
fruits.add("orange")
fruits.remove("banana")

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)                        # union: {1, 2, 3, 4, 5}
print(a & b)                        # intersection: {3}
print(a - b)                        # difference: {1, 2}
```

---

## List

### Definition
An ordered, mutable sequence that can hold any combination of data types. Supports indexing and slicing.

### How It's Used
- Storing ordered collections (queue of tasks, list of names)
- When the data needs to change (add, remove, sort)
- Iterating through items in sequence

### Examples
```python
# Creating a list
shopping = ["milk", "bread", "eggs"]

# Indexing and slicing
print(shopping[0])                  # "milk"
print(shopping[-1])                 # "eggs"
print(shopping[0:2])                # ["milk", "bread"]

# Mutating
shopping.append("butter")
shopping[1] = "bagels"
shopping.remove("eggs")

# Iterating
for item in shopping:
    print(item)

# List comprehension
squares = [n * n for n in range(5)] # [0, 1, 4, 9, 16]
```

---

## String

### Definition
An immutable, ordered sequence of characters. Once created, individual characters cannot be changed.

### How It's Used
- Storing and manipulating text
- Formatting output for users
- Parsing input (file names, user data, etc.)

### Examples
```python
# Creating a string
greeting = "Hello, world!"

# Indexing and slicing
print(greeting[0])                  # "H"
print(greeting[7:12])               # "world"

# Common methods
print(greeting.upper())             # "HELLO, WORLD!"
print(greeting.replace("world", "Python"))  # "Hello, Python!"
print(greeting.split(", "))         # ["Hello", "world!"]

# Concatenation and formatting
name = "Marco"
print("Hi, " + name)
print(f"Hi, {name}")                # f-string

# Strings are immutable
# greeting[0] = "h"  # TypeError
```

---

## Tuple

### Definition
An ordered, immutable sequence that can hold any combination of data types. Like a list, but cannot be changed after creation.

### How It's Used
- Returning multiple values from a function
- Storing fixed records (coordinates, RGB colors, database rows)
- Keys in a dictionary (since they're immutable)

### Examples
```python
# Creating a tuple
point = (3, 4)
rgb = (255, 128, 0)

# Indexing
print(point[0])                     # 3

# Unpacking
x, y = point
print(x, y)                         # 3 4

# Returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 9, 1])   # tuple unpacked into two vars

# Tuples as dictionary keys
locations = {(0, 0): "origin", (1, 2): "point A"}
```

---

## When to Use Which?

| Need | Use |
|---|---|
| Look up values by a label | **Dictionary** |
| Check membership / remove duplicates | **Set** |
| Ordered, changeable collection | **List** |
| Work with text | **String** |
| Fixed, ordered group of values | **Tuple** |

---

# Dictionary Study Guide

This study guide provides a quick-reference summary of the Dictionary lesson and serves as a guide for the practice quiz. It covers the properties of the Python dictionary data type, how dictionaries differ from lists, how to iterate over the contents of a dictionary, and how to use dictionaries with lists and strings.

## Knowledge

Python dictionaries are used to organize elements into collections. Dictionaries include one or more keys, with one or more values associated with each key.

### Syntax

```python
my_dictionary = {"keyA": ["value1", "value2"], "keyB": ["value3", "value4"]}
```

---

## Operations

| Operation | Description |
|---|---|
| `len(dictionary)` | Returns the number of items in a dictionary. |
| `for key in dictionary` | Iterates over each key in a dictionary. |
| `for key, value in dictionary.items()` | Iterates over each key/value pair in a dictionary. |
| `if key in dictionary` | Checks whether a key is in a dictionary. |
| `dictionary[key]` | Accesses a value using the associated key. |
| `dictionary[key] = value` | Sets a value associated with a key. |
| `del dictionary[key]` | Removes a value using the associated key. |
| `merged_dict = dict1 \| dict2` | **Merge operator** — creates a new dictionary with combined items. If both share a key, the value from `dict2` (right side) wins. (Python 3.9+) |
| `dict1 \|= dict2` | **Update operator** — updates the original dictionary in place with items from another. (Python 3.9+) |

---

## Methods

| Method | Description |
|---|---|
| `dictionary.get(key, default)` | Returns the value for a key, or the default if the key is missing. |
| `dictionary.keys()` | Returns a live view of the keys. Iterable but not indexable (cannot use `[0]`). |
| `dictionary.values()` | Returns a view object of the values. Updates automatically if the dictionary changes. |
| `dictionary[key].append(value)` | Appends a new value for an existing key — only works if the value is a mutable sequence (e.g., a list). |
| `dictionary.update(other_dictionary)` | Updates a dictionary with items from another. Existing entries are updated; new entries are added. |
| `dictionary.clear()` | Deletes all items from a dictionary. |
| `dictionary.copy()` | Makes a copy of a dictionary. |

---

## Dictionaries versus Lists

### Both dictionaries and lists
- Organize elements into collections.
- Use empty brackets to initialize a new dictionary or list.
- Can be iterated through.
- Support methods and operations to create and change the collections (removing, inserting, etc.).

### Dictionaries only
- **Preserve insertion order** (Python 3.7+). On legacy systems (Python 3.5 or older), dictionaries are completely unordered.
- Keys can be a variety of data types: strings, integers, floats, tuples.
- Access values by **keys** (not by position).
- Use curly brackets `{ }` to define the dictionary and square brackets `[ ]` to access specific keys.
- Use colons `:` between the key and the value(s).
- Use commas to separate each key group and each value within a key group.
- Support **nested collections** — store a list as a value for "one-to-many" relationships (e.g., one key having a list of several values).
- Faster lookups for specific elements compared to a list.

**Dictionary Example:**
```python
pet_dictionary = {
    "dogs": ["Yorkie", "Collie", "Bulldog"],
    "cats": ["Persian", "Scottish Fold", "Siberian"],
    "rabbits": ["Angora", "Holland Lop", "Harlequin"]
}
print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']
```

In `{"dogs": ["Yorkie", "Collie"]}`, the curly brackets `{ }` are the container for the whole dictionary. The square brackets `[ ]` are a sub-container for the list of values assigned to that key.

### Lists only
- Are **ordered** sets.
- Access elements by **index** positions.
- Indices must be integers.
- Use square brackets `[ ]`.
- Use commas to separate each element.

**List Example:**
```python
pet_list = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish Fold",
            "Siberian", "Angora", "Holland Lop", "Harlequin"]
print(pet_list[0:3])
# Should print ['Yorkie', 'Collie', 'Bulldog']
```

---

## Coding Skills

### Skill Group 1 — Sum dictionary values with `.items()`

Iterate over key/value pairs of a dictionary using a `for` loop with the `dictionary.items()` method to calculate the sum of all values.

```python
# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.
def sum_server_use_time(Server):
    # Initialize as a float — holds the sum of usage hours.
    total_use_time = 0.0

    # Iterate through key/value items.
    for key, value in Server.items():
        # Add each user's time to the running total.
        total_use_time += value

    # Round to 2 decimal places.
    return round(total_use_time, 2)


FileServer = {
    "EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1,
    "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8
}
print(sum_server_use_time(FileServer))  # Should print 20.1
```

### Skill Group 2 — Build a flat list from a dict-of-lists

Concatenate a value, a string, and the key for each item in the dictionary and append to a new list using `list.append()`. Iterate over keys with multiple values using **nested for loops** with `dictionary.items()`.

```python
# Receives a dictionary of last_name -> [first_names].
# Returns a flat list of full names: "First Last".
def list_full_names(employee_dictionary):
    full_names = []

    # Outer loop: each last_name key and its list of first_names.
    for last_name, first_names in employee_dictionary.items():

        # Inner loop: each first_name in the current list.
        for first_name in first_names:
            full_names.append(first_name + " " + last_name)

    return full_names


print(list_full_names({
    "Ali": ["Muhammad", "Amir", "Malik"],
    "Devi": ["Ram", "Amaira"],
    "Chen": ["Feng", "Li"]
}))
# Should print:
# ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']
```

### Skill Group 3 — Invert a dict-of-lists

Use `dictionary[key] = value` to associate a value with a key. Iterate over keys with multiple values using nested for loops + an `if` statement and `dictionary.items()`. Use `dictionary[key].append(value)` to add to an existing key's list.

```python
# Receives a dictionary of category -> [resources].
# Returns a dictionary of resource -> [categories it belongs to].
def invert_resource_dict(resource_dictionary):
    new_dictionary = {}

    # Outer loop: each category and its list of resources.
    for resource_group, resources in resource_dictionary.items():

        # Inner loop: each resource in the list.
        for resource in resources:
            # If resource already a key, append the category to its list.
            if resource in new_dictionary:
                new_dictionary[resource].append(resource_group)
            # Otherwise, create a new key with a single-item list.
            else:
                new_dictionary[resource] = [resource_group]

    return new_dictionary


print(invert_resource_dict({
    "Hard Drives": ["IDE HDDs", "SCSI HDDs"],
    "PC Parts": ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"],
    "Video Cards": ["High-end video cards", "Basic video cards"]
}))
# Should print:
# {'IDE HDDs': ['Hard Drives', 'PC Parts'],
#  'SCSI HDDs': ['Hard Drives', 'PC Parts'],
#  'High-end video cards': ['PC Parts', 'Video Cards'],
#  'Basic video cards': ['PC Parts', 'Video Cards']}
```

---

## Resources

- **[Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)** — Official python.org documentation for dictionary methods.
- **[Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)** — Tutorial with interactive code blocks for practicing dictionary methods and operations.
