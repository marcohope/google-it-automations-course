# =============================================
# Annotating Variables — type hints & dynamic typing
# =============================================

# ---------- Type hints (PEP 484) ----------
name: str = "Betty"
age: int = 34


# ---------- Dynamic typing ----------
# A variable's type can change at runtime.
a = 3              # a is an integer
a = "Hello World"  # a is now a string


# ---------- Duck typing ----------
# "If it walks like a duck and quacks like a duck, it's a duck."
a = "Hello World"  # looks like a string, acts like a string → it's a string


# ---------- Type comments (alternative syntax) ----------
captain = "Jack Sparrow"  # type: str
