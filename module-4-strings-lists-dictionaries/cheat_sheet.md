# Module 4 Cheat Sheet — Strings, Lists & Dictionaries

---

## STRINGS

### Methods & Functions
| Method/Func | What it does | Example |
|---|---|---|
| `.upper()` | All uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All lowercase | `"HI".lower()` → `"hi"` |
| `.split()` | Split into list by whitespace (or delimiter) | `"a b c".split()` → `["a","b","c"]` |
| `.strip()` | Remove leading/trailing whitespace | `" hi ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace substring | `"cat".replace("cat","CAT")` → `"CAT"` |
| `.format()` | Inject variables into `{}` placeholders | `"{} is {}".format("x", 1)` → `"x is 1"` |
| `.isalpha()` | True if all letters | `"abc".isalpha()` → `True` |
| `.isnumeric()` | True if all digits | `"123".isnumeric()` → `True` |
| `len(s)` | Length of string | `len("hi")` → `2` |
| `s[i]` | Index a character | `"abc"[1]` → `"b"` |
| `s[start:end]` | Slice (end is **exclusive**) | `"abcde"[1:3]` → `"bc"` |

### Key Patterns
```python
# Replace a word with its uppercase version
sentence.replace("word", "word".upper())

# Split string, test each part, build new vars
for x in text.split():
    if x.isalpha():
        item += x + " "
    else:
        price = x
item = item.strip()

# Count letters with a dictionary
freq = {}
for ch in string:
    freq[ch] = freq.get(ch, 0) + 1
```

---

## LISTS

### Methods
| Method | What it does | Example |
|---|---|---|
| `.append(x)` | Add x to end | `lst.append(4)` |
| `.insert(i, x)` | Insert x at index i | `lst.insert(1, "a")` → inserts "a" at index 1, shifts rest right |
| `.remove(x)` | Remove first occurrence of x | `lst.remove(3)` |
| `.reverse()` | Reverse **in place** | `lst.reverse()` |
| `.extend(lst2)` | Append all items of lst2 | `lst.extend([4,5])` |
| `.sort()` | Sort **in place** | `lst.sort()` |

### List Comprehensions
```python
# Basic — new list from range
[year for year in range(start, end+1)]

# With if condition
[n for n in range(x, y) if n % 2 != 0]   # odd numbers from x to y-1
```

### Key Pattern: reverse + extend to merge two lists
```python
recent_first.reverse()           # flip to chronological
recent_last.extend(recent_first) # append onto older list
```

---

## DICTIONARIES

### Methods & Operations
| Method/Op | What it does | Example |
|---|---|---|
| `d[key]` | Get value by key | `d["name"]` |
| `d[key] = val` | Set/update a value | `d["score"] = 0` |
| `.keys()` | List of keys | `d.keys()` |
| `.values()` | List of values | `d.values()` |
| `.items()` | List of `(key, value)` tuples | `for k, v in d.items()` |
| `.update({k:v})` | Merge another dict in | `d.update({"x": 1})` |
| `.copy()` | Shallow copy | `new = d.copy()` |

### Key Patterns
```python
# Iterate and format key-value pairs
for hostname, ip in servers.items():
    result += "The IP of {} is {}".format(hostname, ip) + "\n"

# Copy and reset all values to 0
new = original.copy()
for player, score in new.items():
    new[player] = 0

# Print all keys as a list
print(list(d.keys()))

# Count letter frequency
freq = {}
for ch in string:
    freq[ch] = freq.get(ch, 0) + 1
```

---

## COMMON SYNTAX ERRORS TO AVOID

| Error | Example of mistake |
|---|---|
| Misspelling | `.apend()` instead of `.append()` |
| Wrong case | `true` instead of `True` |
| Bad indentation | Missing 4-space indent inside `for`/`if` |
| Wrong bracket | `d("key")` instead of `d["key"]` |
| Missing colon | `for x in lst` instead of `for x in lst:` |
| Slice off-by-one | `s[1:3]` → indices 1 & 2 only (3 excluded) |
| Quote mismatch | `"hello'` |
| Type mismatch | `"price: " + 9.99` (need `str(9.99)`) |
