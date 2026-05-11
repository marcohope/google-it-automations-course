# =============================================
# elif Statements — collapsing nested if/else
# =============================================

# ---------- Nested if/else (verbose) ----------
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     else:
#         if len(username) > 15:
#             print("Invalid username. Must be at most 15 characters long")
#         else:
#             print("Valid username")


# ---------- Refactored with elif (cleaner) ----------
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")


# ---------- Test ----------
hint_username("ma")              # too short
hint_username("marco")           # valid
hint_username("marco" * 5)       # too long
