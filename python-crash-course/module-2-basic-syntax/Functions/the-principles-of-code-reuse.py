# =============================================
# The Principles of Code Reuse
# Same logic repeated → factor it into a function (DRY)
# =============================================

# ---------- Repeated code (avoid) ----------
name = "Kay"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))


# ---------- Refactored with a function ----------
# def lucky_number(name):
#     number = len(name) * 9
#     print("Hello " + name + ". Your lucky number is " + str(number))
#
# lucky_number("Kay")
# lucky_number("Cameron")
