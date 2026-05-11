# =============================================
# Modifying Lists — append, insert, remove, pop, index assignment
# Lists are MUTABLE: you can change them in place.
# =============================================

fruits = ["Pineapple", "Banana", "Apple", "Melon"]


# ---------- .append() — add to the end ----------
fruits.append("Kiwi")
print(fruits)
# ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']


# ---------- .insert(index, item) — add at a specific position ----------
fruits.insert(0, "Orange")
print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']


# ---------- .remove(value) — remove first matching value ----------
fruits.remove("Pineapple")
print(fruits)
# ['Orange', 'Banana', 'Apple', 'Melon', 'Kiwi']


# ---------- .pop(index) — remove element at index ----------
fruits.pop(3)             # removes 'Melon'
print(fruits)
# ['Orange', 'Banana', 'Apple', 'Kiwi']


# ---------- Index assignment — replace an item ----------
fruits[2] = "Strawberry"  # 'Apple' → 'Strawberry'
print(fruits)
# ['Orange', 'Banana', 'Strawberry', 'Kiwi']
