# =============================================
# Looping Through Strings
# Three ways to iterate over the characters of a string
# =============================================

# ---------- Approach 1: for char in string ----------
# greeting = 'Hello'
# for char in greeting:
#     print(char)


# ---------- Approach 2: for i in range(len(string)) ----------
# for i in range(len(greeting)):
#     print(i)


# ---------- Approach 3: while loop with index ----------
# greeting = 'Hello'
# index = 0
# while index < len(greeting):
#     print(greeting[index])
#     index += 1


# ---------- Active example: while loop with slicing ----------
# NOTE: `index += 1` must be inside the while block, otherwise the loop
# is infinite (it never advances). Keep this indented.
greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index + 1])
    index += 1
