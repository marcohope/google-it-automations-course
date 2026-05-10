# x = {}
# print(type(x))

file_counts = {"jpg":10, "txt": 14, "csv":2, "py":23}
#storing strings that point at integer values
# print(file_counts)
print(file_counts["txt"])

print("jpg" in file_counts)


## Dictionaries are mutable

file_counts["xml"] = 8

print(file_counts)

## if you try to add a key that already exists it overrides the preexisiting key

file_counts["csv"] = 13

print(file_counts)

## you can delete keys as well with del

del file_counts["py"]

print(file_counts)

print("csv" in file_counts)