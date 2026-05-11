# =============================================
# Practice — Looping through a string for vowels
# =============================================

text = "Four score and seven years ago"


# ---------- Approach 1: for loop with condition ----------
for c in text:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(c)


# ---------- Approach 2: list comprehension ----------
print([c for c in text if c.lower() in ['a', 'e', 'i', 'o', 'u']])


# ---------- Approach 3: count occurrences ----------
# .count() only counts the exact substring "aeiou", not each vowel — so this is 0
print(text.count("aeiou"))
