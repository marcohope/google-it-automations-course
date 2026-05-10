fullname = ('Grace', 'M', 'Hopper')
#immutable sequence of elements
#position in elemnts have meaning
def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
type(result)

# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return hours, minutes, remaining_seconds
# result = convert_seconds(5000)
# print(result)

# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return hours, minutes, remaining_seconds
# result = convert_seconds(5000)
# hours, minutes, seconds = result
# print(hours, minutes, seconds)

# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return hours, minutes, remaining_seconds
# hours, minutes, seconds = convert_seconds(1000)
# print(hours, minutes, seconds)

