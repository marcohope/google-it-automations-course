
# Python Major Data Types

# 1. Integer (int): Whole numbers without decimal points
print("=== Integer (int) ===")
print(type(5))  # <class 'int'>
int_example = 42
negative_int = -10
print(f"Examples: {int_example}, {negative_int}")

# 2. Float: Decimal numbers
print("\n=== Float ===")
print(type(5.0))  # <class 'float'>
float_example = 3.14
negative_float = -2.5
print(f"Examples: {float_example}, {negative_float}")

# 3. String (str): Text data enclosed in quotes
print("\n=== String (str) ===")
print(type("five"))  # <class 'str'>
str_example1 = "Hello, World!"
str_example2 = 'Single quotes work too'
str_example3 = """Multi-line
strings use triple quotes"""
print(f"Examples: {str_example1}, {str_example2}")

# 4. Boolean (bool): True or False values
print("\n=== Boolean (bool) ===")
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>
bool_example1 = True
bool_example2 = False
print(f"Examples: {bool_example1}, {bool_example2}")

# 5. NoneType: Represents the absence of a value
print("\n=== NoneType ===")
print(type(None))  # <class 'NoneType'>
none_example = None
print(f"Example: {none_example}")

# 6. List: Ordered, mutable collection of items (can be modified)
print("\n=== List ===")
print(type([1, 2, 3]))  # <class 'list'>
list_example1 = [1, 2, 3, 4, 5]
list_example2 = ["apple", "banana", "cherry"]
list_example3 = [1, "mixed", 3.14, True, None]  # Can contain different types
print(f"Examples: {list_example1}, {list_example2}")

# 7. Tuple: Ordered, immutable collection of items (cannot be modified)
print("\n=== Tuple ===")
print(type((1, 2, 3)))  # <class 'tuple'>
tuple_example1 = (1, 2, 3)
tuple_example2 = ("red", "green", "blue")
tuple_example3 = (42,)  # Single element tuple requires a comma
print(f"Examples: {tuple_example1}, {tuple_example2}")

# 8. Dictionary (dict): Unordered collection of key-value pairs
print("\n=== Dictionary (dict) ===")
print(type({'name': 'Alice', 'age': 30}))  # <class 'dict'>
dict_example1 = {'name': 'Alice', 'age': 30}
dict_example2 = {'product': 'laptop', 'price': 999.99, 'in_stock': True}
print(f"Examples: {dict_example1}")

# 9. Set: Unordered collection of unique items
print("\n=== Set ===")
print(type({1, 2, 3}))  # <class 'set'>
set_example1 = {1, 2, 3, 4, 5}
set_example2 = {"apple", "banana", "cherry"}
set_example3 = {1, 2, 2, 3, 3, 3}  # Duplicates are removed
print(f"Examples: {set_example1}, {set_example2}")

# 10. Range: Sequence of numbers generated on-the-fly
print("\n=== Range ===")
print(type(range(5)))  # <class 'range'>
range_example1 = range(5)  # 0, 1, 2, 3, 4
range_example2 = range(1, 10, 2)  # 1, 3, 5, 7, 9
print(f"Examples: {list(range_example1)}, {list(range_example2)}")

# 11. Function/Callable: Functions and built-in methods
print("\n=== Function/Callable ===")
print(type(len))  # <class 'builtin_function_or_method'>
print(type(print))  # <class 'builtin_function_or_method'>
def my_function():
    return "Hello"
print(type(my_function))  # <class 'function'>
