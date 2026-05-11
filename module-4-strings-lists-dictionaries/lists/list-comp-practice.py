# =============================================
# List Comprehension — Practice
# Function that returns squares of numbers from start to end (inclusive)
# =============================================

def squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


# ---------- Tests ----------
print(squares(2, 3))     # [4, 9]
print(squares(1, 5))     # [1, 4, 9, 16, 25]
print(squares(0, 10))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
