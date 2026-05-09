def converting_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaning_seconds = (seconds - hours * 3600 - minutes * 60)
    return hours, minutes, remaning_seconds

hours, minutes, seconds = converting_seconds(5000)
print(hours, minutes, seconds)
