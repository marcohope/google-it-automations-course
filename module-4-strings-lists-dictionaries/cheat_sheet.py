# ============================================================
#  MODULE 4 CHEAT SHEET — Strings, Lists, Dictionaries
#  Run any section to see output. Comment/uncomment as needed.
# ============================================================


# ────────────────────────────────────────────────────────────
#  STRINGS
# ────────────────────────────────────────────────────────────

s = "Hello World 123"

print(s.upper())            # HELLO WORLD 123
print(s.lower())            # hello world 123
print(s.split())            # ['Hello', 'World', '123']
print(s.replace("World", "Python"))  # Hello Python 123
print("  hi  ".strip())     # 'hi'
print(s[0])                 # H        (index)
print(s[0:5])               # Hello    (slice — end is exclusive)
print(len(s))               # 15
print("abc".isalpha())      # True
print("123".isnumeric())    # True
print("{} costs ${}".format("Apple", 1.99))  # Apple costs $1.99

# Replace a word with its uppercase version
sentence = "the quick brown fox"
print(sentence.replace("fox", "fox".upper()))  # the quick brown FOX

# Split string → separate letters from numbers
text = "Winter jacket 49.99"
item, price = "", ""
for x in text.split():
    if x.isalpha():
        item += x + " "
    else:
        price = x
item = item.strip()
print("{} are on sale for ${}".format(item, price))
# Winter jacket are on sale for $49.99


# ────────────────────────────────────────────────────────────
#  LISTS
# ────────────────────────────────────────────────────────────

lst = [3, 1, 4, 1, 5]

lst.append(9)       # [3, 1, 4, 1, 5, 9]     — add to end
lst.insert(1, 99)   # [3, 99, 1, 4, 1, 5, 9] — insert at index 1
lst.remove(1)       # removes first occurrence of 1
lst.sort()          # sorts in place
lst.reverse()       # reverses in place
print(lst)

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)         # a is now [1, 2, 3, 4, 5, 6]
print(a)

# Merge two lists in chronological order
recent_first = [2022, 2018, 2011, 2006]
recent_last  = [1989, 1992, 1997, 2001]
recent_first.reverse()
recent_last.extend(recent_first)
print(recent_last)  # [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]

# List comprehension — basic
years = [y for y in range(1972, 1976)]
print(years)        # [1972, 1973, 1974, 1975]

# List comprehension — with if condition
odds = [n for n in range(5, 15) if n % 2 != 0]
print(odds)         # [5, 7, 9, 11, 13]


# ────────────────────────────────────────────────────────────
#  DICTIONARIES
# ────────────────────────────────────────────────────────────

d = {"a": 1, "b": 2, "c": 3}

print(d["a"])           # 1              — get value
d["d"] = 4              # add/update key
print(list(d.keys()))   # ['a', 'b', 'c', 'd']
print(list(d.values())) # [1, 2, 3, 4]

d.update({"e": 5})      # merge in another dict
print(d)

# Iterate key-value pairs
servers = {"DNS": "8.8.8.8", "Gateway": "192.168.1.1"}
for hostname, ip in servers.items():
    print("The IP of the {} server is {}".format(hostname, ip))

# Copy and reset all values
scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
new_scores = scores.copy()
for player in new_scores:
    new_scores[player] = 0
print(new_scores)   # {'Arshi': 0, 'Catalina': 0, 'Diego': 0}

# Count letter frequency
freq = {}
for ch in "hello":
    freq[ch] = freq.get(ch, 0) + 1
print(freq)         # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
