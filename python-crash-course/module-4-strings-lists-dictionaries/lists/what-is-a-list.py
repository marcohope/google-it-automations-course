# =============================================
# What is a List?
# An ordered, mutable sequence of items.
# =============================================

x = ["Now", "we", "are", "cooking!"]


# ---------- type() ----------
print(type(x))           # <class 'list'>


# ---------- print() ----------
print(x)                 # ['Now', 'we', 'are', 'cooking!']


# ---------- len() ----------
print(len(x))            # 4


# ---------- Membership: `in` ----------
print("are" in x)        # True
print("Today" in x)      # False


# ---------- Indexing (0-based) ----------
print(x[0])              # 'Now'
print(x[3])              # 'cooking!'
# print(x[4])            # IndexError — out of range


# ---------- Slicing ----------
print(x[1:3])            # ['we', 'are']    (indices 1, 2)
print(x[:2])             # ['Now', 'we']    (start through 1)
print(x[2:])             # ['are', 'cooking!']  (index 2 to end)
