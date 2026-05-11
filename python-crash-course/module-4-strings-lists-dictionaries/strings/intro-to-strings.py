# =============================================
# Intro to Strings
# =============================================

# ---------- Defining strings ----------
# Strings can use single or double quotes — but they must match
name = "Sasha"
color = 'Gold'

# place = "Cambridge'   # SyntaxError — quote types mismatch

# Empty string
pet = ""


# ---------- Concatenation ----------
print("Name: " + name + ", Favorite color: " + color)


# ---------- Repetition with * ----------
print("example" * 3)        # 'exampleexampleexample'


# ---------- len() — number of characters ----------
pet = "loooooooooooooooooooooooooooooooong cat"
print(len(pet))             # 39
