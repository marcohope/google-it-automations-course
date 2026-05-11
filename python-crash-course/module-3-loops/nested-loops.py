# =============================================
# Nested Loops
# A loop inside a loop — runs the inner loop fully
# for every iteration of the outer loop.
# =============================================


# ---------- Example 1: a grid of pairs ----------
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()   # newline at the end of each row


# ---------- Example 2: all team matchups (no self-matches) ----------
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


# ---------- Pattern reference ----------
# Single loop — O(n)
# for element in long_list:
#     do_something(element)
#
# Nested loop — O(n²)
# for element1 in long_list:
#     for element2 in long_list:
#         do_something(element1, element2)
