for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

  teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

# for element in long_list:
#   do_something(element)

# for element1 in long_list:
#   for element2 in long_list:
#     do_something(element1, element2)

