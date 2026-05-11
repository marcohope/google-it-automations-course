# =============================================
# Formatting Strings — .format() and format specifiers
# =============================================

# ---------- Positional placeholders ----------
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))


# ---------- Named placeholders ----------
name = "Manny"
print("Your lucky number is {number}, {name}.".format(
    name=name,
    number=len(name) * 3,
))


# ---------- Format specifiers — decimal places ----------
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


# ---------- Format specifiers — width & alignment ----------
# {:>3}    right-aligned, min width 3
# {:>6.2f} right-aligned, min width 6, 2 decimal places
def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
