# =============================================
# Lists and Tuples
# Tuple: immutable sequence — order matters, positions have meaning
# List:  mutable sequence  — can grow/shrink/change in place
# =============================================

# ---------- Tuple example ----------
fullname = ('Grace', 'M', 'Hopper')


# ---------- Functions returning multiple values (as a tuple) ----------
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


# ---------- Capture the returned tuple ----------
result = convert_seconds(5000)
print(type(result))     # <class 'tuple'>
print(result)           # (1, 23, 20)


# ---------- Unpacking the tuple into variables ----------
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)   # 0 16 40
