# =============================================
# Code Style — naming & readability
# =============================================

# ---------- Bad: cryptic names ----------
# def calculate(d):
#     q = 3.14
#     z = q * (d ** 2)
#     print(z)
# Output is 78.5


# ---------- Good: descriptive names ----------
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area


print(circle_area(5))   # 78.5
