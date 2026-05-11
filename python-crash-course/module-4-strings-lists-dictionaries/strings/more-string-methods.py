# =============================================
# More String Methods
# =============================================

# ---------- .upper() / .lower() — change case ----------
print("Mountains".upper())          # MOUNTAINS
print("Mountains".lower())          # mountains


# ---------- Normalizing case for comparison ----------
answer = "YES"
if answer.lower() == "yes":
    print("User said yes")


# ---------- .strip() / .lstrip() / .rstrip() — remove whitespace ----------
print(" yes ".strip())              # 'yes'
print(" yes ".lstrip())             # 'yes ' (left-only)
print(" yes ".rstrip())             # ' yes' (right-only)


# ---------- .count() — count occurrences of a substring ----------
print("The number of times e occurs in this string is 4".count("e"))   # 4


# ---------- .endswith() / .startswith() ----------
print("Forest".endswith("rest"))    # True


# ---------- .isnumeric() — only digits? ----------
print("Forest".isnumeric())         # False
print("12345".isnumeric())          # True

# Combine with int() to convert numeric strings to ints
print(int("12345") + int("54321"))  # 66666


# ---------- .join() — combine list of strings ----------
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))


# ---------- .split() — break a string into a list ----------
print("This is another example".split())
# ['This', 'is', 'another', 'example']
