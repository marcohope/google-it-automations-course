# Module 4 — Strings: Study Guide

---

## What is a String?

A string is an **immutable**, ordered sequence of characters. Strings can be defined with single or double quotes — they must match.

```python
name  = "Sasha"
color = 'Gold'
empty = ""
```

Strings can be **repeated**:

```python
"ha" * 3   # "hahaha"
```

Get the **length** with `len()`:

```python
len("Pineapple")  # 9
```

---

## Indexing

Access a single character by its position (zero-based):

```python
name = "Jaylen"
print(name[0])   # J
print(name[1])   # a
print(name[5])   # n
```

Negative indices count from the end:

```python
text = "Random string with a lot of characters"
print(text[-1])  # s (last character)
print(text[-2])  # r
```

> Accessing an index beyond the length raises an `IndexError`.

---

## Slicing

Extract a substring with `[start:end]` — includes `start`, excludes `end`.

```python
fruit = "Pineapple"
print(fruit[:4])   # Pine     (from 0 up to 4)
print(fruit[4:])   # apple    (from 4 to end)
print(fruit[2:6])  # neap
```

| Slice | Meaning |
|---|---|
| `s[x]` | Single character at index `x` |
| `s[x:y]` | From index `x` up to (not including) `y` |
| `s[:y]` | From start up to `y` |
| `s[x:]` | From `x` to end |
| `s[-n:]` | Last `n` characters |

---

## Strings are Immutable

You **cannot** change a character in place:

```python
message = "A kong string with a silly typo"
message[2] = "l"   # TypeError!
```

Instead, build a new string:

```python
new_message = message[0:2] + "l" + message[3:]
print(new_message)  # A long string with a silly typo
```

---

## Basic String Methods

| Method | Description | Example |
|---|---|---|
| `.upper()` | All uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All lowercase | `"HELLO".lower()` → `"hello"` |
| `.strip()` | Remove leading/trailing whitespace | `" yes ".strip()` → `"yes"` |
| `.lstrip()` | Remove leading whitespace | `" yes ".lstrip()` → `"yes "` |
| `.rstrip()` | Remove trailing whitespace | `" yes ".rstrip()` → `" yes"` |
| `.count(sub)` | Count occurrences of `sub` | `"abcabc".count("a")` → `2` |
| `.endswith(sub)` | Check if ends with `sub` | `"Forest".endswith("rest")` → `True` |
| `.isnumeric()` | Check if all characters are digits | `"123".isnumeric()` → `True` |
| `.index(sub)` | First index of `sub` (raises error if not found) | `"lions tigers".index("g")` → `8` |

```python
answer = "YES"
if answer.lower() == "yes":
    print("User said yes")
```

---

## `in` Operator

Check if a substring exists:

```python
animals = "lions tigers and bears"
print("tigers" in animals)   # True
print("horses" in animals)   # False
```

---

## More String Methods

| Method | Description | Example |
|---|---|---|
| `.join(iterable)` | Joins elements with the string as separator | `" ".join(["a","b","c"])` → `"a b c"` |
| `.split(sep)` | Splits string into a list (default: whitespace) | `"a b c".split()` → `["a","b","c"]` |
| `.replace(old, new)` | Replaces all occurrences of `old` with `new` | `"foo".replace("o","0")` → `"f00"` |

```python
" ".join(["This", "is", "a", "phrase"])
# "This is a phrase"

"...".join(["This", "is", "joined", "by", "dots"])
# "This...is...joined...by...dots"

"This is another example".split()
# ["This", "is", "another", "example"]
```

---

## Creating New Strings with Slicing + Index

```python
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
```

---

## String Formatting

### `.format()` Method

```python
name   = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

# Named placeholders
print("Your lucky number is {number}, {name}.".format(name=name, number=number))
```

### Format Specifiers

```python
price    = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# Base price: $7.50. With Tax: $8.18
```

| Specifier | Meaning |
|---|---|
| `{:.2f}` | Float rounded to 2 decimal places |
| `{:>3}` | Right-aligned in a field of width 3 |
| `{:<3}` | Left-aligned in a field of width 3 |

```python
def to_celsius(x):
    return (x - 32) * 5 / 9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
```

### f-Strings (Python 3.6+)

```python
name = "Marco"
age  = 20
print(f"Hello, {name}! You are {age} years old.")
```

---

## Practical Patterns

### Vowel filter using a loop

```python
input_str = "Four score and seven years ago"
for c in input_str:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(c)
```

### String slicing to rearrange

```python
# Move first character to end, add a dash
def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
    return new_string

print(change_string("1one 2two 3three"))  # "one-1 two-2 three-3 "
```

---

## Key Concepts Checklist

- [ ] Access characters with `string[index]` (positive and negative)
- [ ] Slice strings with `string[start:end]`
- [ ] Understand strings are immutable — build new strings instead
- [ ] Use `.upper()`, `.lower()`, `.strip()` for normalization
- [ ] Use `.index()` and `in` to search within strings
- [ ] Use `.split()` to break a string into a list
- [ ] Use `.join()` to combine a list into a string
- [ ] Use `.replace()` to substitute substrings
- [ ] Use `.format()` or f-strings to build formatted output
- [ ] Use format specifiers like `{:.2f}` and `{:>n}`
