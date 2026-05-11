# =============================================
# List Comprehensions
# Compact way to build a list from a sequence.
# Syntax: [expression for item in iterable (if condition)]
# =============================================

# ---------- Without a comprehension (for loop + append) ----------
# multiples = []
# for x in range(1, 11):
#     multiples.append(x * 7)
# print(multiples)


# ---------- Same thing, as a comprehension ----------
# multiples = [x * 7 for x in range(1, 11)]
# print(multiples)


# ---------- Building a list of lengths ----------
# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)


# ---------- With a condition (filter) ----------
# multiples of 3 from 0 to 100
# z = [x for x in range(0, 101) if x % 3 == 0]
# print(z)

# names = ["Marco", "Scott", "Micheal", "Nick"]
# lengths = [len(name) for name in names]
# print(lengths)


# ---------- Active example: multiples of 4 from 0 to 100 ----------
z = [x for x in range(0, 101) if x % 4 == 0]
print(z)


# ---------- Rule of thumb ----------
# Use list comprehensions for simple logic that fits on one line.
# Use a regular for-loop when the logic is more complex.
