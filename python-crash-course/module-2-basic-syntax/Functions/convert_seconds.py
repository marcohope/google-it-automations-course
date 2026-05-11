# =============================================
# Convert Seconds — returning multiple values
# =============================================

def converting_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


# ---------- Test ----------
hours, minutes, seconds = converting_seconds(5000)
print(hours, minutes, seconds)   # 1 23 20
