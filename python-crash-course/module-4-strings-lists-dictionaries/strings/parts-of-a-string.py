# =============================================
# Parts of a String — indexing & slicing
# =============================================

# ---------- Positive indexing (0-based) ----------
name = "Jaylen"
print(name[1])       # 'a'
print(name[0])       # 'J'

print(name[5])       # 'n'  (last char)
# print(name[6])     # IndexError — out of range


# ---------- Negative indexing (from the end) ----------
text = "Random string with a lot of characters"
print(text[-1])      # 's'  (last char)
print(text[-2])      # 'r'  (second-to-last)


# ---------- Slicing: string[start:end] ----------
color = "Orange"
print(color[1:4])    # 'ran'  (indices 1, 2, 3 — end is exclusive)


# ---------- Omitting start or end ----------
fruit = "Pineapple"
print(fruit[:4])     # 'Pine'   (from start to index 4)
print(fruit[4:])     # 'apple'  (from index 4 to end)
