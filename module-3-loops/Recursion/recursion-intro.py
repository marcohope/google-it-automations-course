# =============================================
# Recursion — Intro
# A function that calls itself with a smaller problem
# until it reaches a base case.
# =============================================

def sum_positive_nums(n):
    # Base case — stop recursing
    if n < 1:
        return 0
    # Recursive case — n + sum of everything below
    return n + sum_positive_nums(n - 1)


# ---------- Tests ----------
print(sum_positive_nums(5))    # 15  (1+2+3+4+5)
print(sum_positive_nums(10))   # 55  (1+2+...+10)
