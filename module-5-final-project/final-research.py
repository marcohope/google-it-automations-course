numbers = [ 4, 6, 2, 7, 1 ]
numbers.sort()
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names)) # sorted by alpha order
print(names) #print list
print(sorted(names, key=len)) # sorted by length of name

# sort() returns nothing because it changes the original list in place
# ^ modifies current list
# sorted() returns a new sorted list