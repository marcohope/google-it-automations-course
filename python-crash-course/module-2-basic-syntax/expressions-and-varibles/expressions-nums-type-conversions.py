# =============================================
# Expressions, Numbers & Type Conversions
# =============================================

# ---------- Implicit conversion ----------
# Python automatically converts types when it can (e.g., int + float)
# print(7 + 5.5)
# print("a" + "b" + "c")
# print("This" + " " + "cat" + " " + "is" + " " + "in" + " " + "the" + " " + "tree")


# ---------- Explicit conversion ----------
# Use str(), int(), float() to convert manually
# base = 6
# height = 3
# area = (base * height) / 2
# print("The area of the triangle is " + str(area))

# Common conversion functions:
#   str()   — converts a value to a string
#   int()   — converts a value to an integer
#   float() — converts a value to a floating point number


# ---------- Practice: average file size ----------
# Directory has 5 files with sizes: 2048, 4357, 97658, 125, 8
# Compute the average and print it.

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The Average size is " + str(average))
