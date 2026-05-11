# =============================================
# Creating New Strings
# Strings are IMMUTABLE — you can't change a character in place.
# To "modify" a string, build a new one with slicing + concatenation.
# =============================================

# ---------- Strings are immutable ----------
# message = "A kong string with a silly typo"
# message[2] = "l"     # TypeError — strings don't support item assignment


# ---------- Build a new string instead ----------
# message = "A kong string with a silly typo"
# new_message = message[0:2] + "l" + message[3:]
# print(new_message)


# ---------- Reassignment creates a new string ----------
# message = "This is a new message"
# print(message)
# message = "And another one"
# print(message)


# ---------- .index() — find the position of a substring ----------
pets = "Cats & Dogs"
print(pets.index("&"))      # 5
# pets.index("x")           # ValueError — substring not found


# ---------- `in` — check if a substring exists (no error) ----------
# print("Dragons" in pets)  # False
# print("Cats" in pets)     # True


# ---------- Real example: replace_domain ----------
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


print(replace_domain("marco@oldsite.com", "oldsite.com", "newsite.com"))
# marco@newsite.com
