# =============================================
# Basic String Methods — index() and `in`
# =============================================

animals = "lions tigers and bears"


# ---------- .index() — returns position of a substring ----------
print(animals.index("g"))         # 8
print(animals.index("bears"))     # 17


# ---------- `in` operator — True/False membership check ----------
print("horses" in animals)        # False
print("tigers" in animals)        # True
