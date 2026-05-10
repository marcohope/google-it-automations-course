# =============================================
# Comparison & Logical Operators
# =============================================

# ---------- Comparison operators ----------
print(10 > 1)              # True
print("cat" == "dog")      # False
print(1 != 2)              # True


# ---------- Type-related comparisons ----------
# print(1 < "1")           # TypeError — can't compare int with str
print(1 == "1")            # False (different types)


# ---------- Logical operators: and / or / not ----------
print("Yellow" > "Cyan" and "Brown" > "Magenta")   # False
print(25 > 50 or 1 != 2)                           # True
print(not 42 == "Answer")                          # True
