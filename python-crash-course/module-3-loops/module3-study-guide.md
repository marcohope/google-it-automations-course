# Module 3 — Loops: Study Guide

---

## 1. `while` Loops

Runs **as long as** a condition is `True`.

```python
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x += 1
print("x=" + str(x))
```

> Always make sure the condition eventually becomes `False` — otherwise you get an **infinite loop**.

### Common Pattern: Counter

```python
count = 1
while count <= 10:
    print(count)
    count += 1
```

### Breaking Out of a Loop

Use `break` to exit early:

```python
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

Use `continue` to skip the rest of the current iteration:

```python
for i in range(10):
    if i % 2 == 0:
        continue     # skip even numbers
    print(i)         # only prints odd numbers
```

---

## 2. `for` Loops

Iterates over a sequence (list, string, range, etc.).

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4
```

### `range()` Parameters

| Call | Output |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 101, 10)` | 0, 10, 20, … 100 |

### Looping Over a List

```python
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
```

### Looping Over a String

```python
greeting = "Hello"
for char in greeting:
    print(char)         # H, e, l, l, o

# With index using range + len
for i in range(len(greeting)):
    print(i, greeting[i])

# With while loop
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1
```

---

## 3. Nested Loops

A loop inside another loop. The inner loop completes fully for each iteration of the outer loop.

```python
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
```

### Practical Example — Round-Robin Schedule

```python
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
```

> **Caution:** Nested loops multiply runtime. If the outer list has `n` items and the inner also has `n`, you get `n²` iterations.

---

## 4. Loop Control: `break` and `continue`

| Keyword | Effect |
|---|---|
| `break` | Exits the loop immediately |
| `continue` | Skips to the next iteration |

```python
# break example
for i in range(10):
    if i == 5:
        break
    print(i)   # prints 0–4 only

# continue example
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # prints odd numbers only
```

---

## 5. Recursion

A function that calls **itself** to solve a smaller version of the same problem. Requires a **base case** to stop.

```python
def sum_positive_nums(n):
    if n < 1:          # base case
        return 0
    return n + sum_positive_nums(n - 1)

print(sum_positive_nums(5))   # 15 (5+4+3+2+1)
print(sum_positive_nums(10))  # 55
```

### Recursion vs. Iteration

| | Recursion | Iteration |
|---|---|---|
| **Uses** | Function calls itself | `for` / `while` loop |
| **Requires** | Base case | Loop condition |
| **Risk** | Stack overflow if too deep | Infinite loop if condition never false |
| **Best for** | Tree traversal, divide-and-conquer | Sequential, counting tasks |

---

## 6. Practical Coding Patterns

### Pattern 1 — Accumulate with a `while` loop

```python
# Sum numbers 1–100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)  # 5050
```

### Pattern 2 — Filter vowels from a string

```python
input_str = "Four score and seven years ago"
vowels = []
for c in input_str:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(c)
print(vowels)

# Same thing as a list comprehension:
print([c for c in input_str if c.lower() in 'aeiou'])
```

### Pattern 3 — Convert seconds to h/m/s

```python
def converting_seconds(seconds):
    hours   = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    secs    = seconds - hours * 3600 - minutes * 60
    return hours, minutes, secs

h, m, s = converting_seconds(5000)
print(h, m, s)  # 1 23 20
```

---

## Key Concepts Checklist

- [ ] Write a `while` loop with a proper exit condition
- [ ] Use `break` to exit a loop early
- [ ] Use `continue` to skip an iteration
- [ ] Write a `for` loop over a range, list, and string
- [ ] Use `range(start, stop, step)`
- [ ] Write and read nested loops
- [ ] Understand the call stack in recursion
- [ ] Write a recursive function with a base case
