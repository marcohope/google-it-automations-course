# =============================================
# else Statements
# =============================================

# ---------- Example 1: if / else ----------
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")


# ---------- Example 2: returning True/False ----------
def is_even(number):
    if number % 2 == 0:
        return True
    return False


# ---------- Tests ----------
hint_username("ma")        # Invalid username...
hint_username("marco")     # Valid username

print(is_even(4))          # True
print(is_even(7))          # False
