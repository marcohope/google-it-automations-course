# =============================================
# Built-in Functions
# Demonstrates: print, type, str, sorted, max, min
# =============================================


# ---------- print() ----------
month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)


# ---------- type() ----------
print(type("This is a string"))


# ---------- str() ----------
number = 12
string_representation = str(number)
print(string_representation)


# ---------- sorted() ----------
# Returns a new sorted list — does NOT modify the original
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)


# ---------- max() and min() ----------
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))
