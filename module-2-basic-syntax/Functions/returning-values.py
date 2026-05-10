# =============================================
# Returning Values — return vs. print
# =============================================

# ---------- Example: returning a calculated value ----------
# def area_triangle(base, height):
#     return 0.5 * base * height
#
# area_a = area_triangle(10, 5)
# area_b = area_triangle(7, 3)
# sum_area = area_a + area_b
#
# print("The area of both triangles is " + str(sum_area))


# ---------- Return statements in Python ----------
# A function without `return` implicitly returns None.

def greeting(name):
    print("Welcome " + name)


result = greeting("christine")
print(result)   # None — greeting() prints but doesn't return a value
