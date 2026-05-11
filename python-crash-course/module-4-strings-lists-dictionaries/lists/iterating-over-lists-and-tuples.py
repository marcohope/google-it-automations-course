# =============================================
# Iterating Over Lists and Tuples
# =============================================

# ---------- Basic for-loop: sum lengths of strings ----------
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(
    chars,
    chars / len(animals),
))


# ---------- enumerate() — get index and value together ----------
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


# ---------- Iterating over a list of tuples (unpacking) ----------
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([
    ("alex@example.com", "Alex Diego"),
    ("shay@example.com", "Shay Brandt"),
]))
