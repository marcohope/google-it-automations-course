# Variable Naming Conventions in Python

## Overview
Variable names in Python must follow specific rules and conventions to be valid. Understanding these restrictions and best practices will help you write cleaner, more maintainable code.

---

## Hard Restrictions (Must Follow)

These are Python language rules. If you violate these, your code will not run.

### 1. Must Start with a Letter or Underscore
- **Must start with:** `a-z`, `A-Z`, or `_`
- **Cannot start with:** numbers or special characters

#### ✅ Valid Examples:
```python
name = "Alice"
_private_var = 42
user_age = 25
MyVariable = 100
```

#### ❌ Invalid Examples:
```python
2nd_place = "silver"  # Starts with number
-value = 10  # Starts with hyphen
@username = "john"  # Starts with special character
#hashtag = "trending"  # Starts with special character
```

### 2. Can Only Contain Alphanumeric Characters and Underscores
- **Allowed:** Letters (`a-z`, `A-Z`), Numbers (`0-9`), and Underscores (`_`)
- **Not allowed:** Spaces, hyphens, special characters, etc.

#### ✅ Valid Examples:
```python
user_name = "John"
score_2024 = 95
_internal_value = 50
Value123 = "test"
```

#### ❌ Invalid Examples:
```python
user-name = "John"  # Contains hyphen
score 2024 = 95  # Contains space
user.name = "John"  # Contains dot
user@name = "John"  # Contains special character
user$value = 10  # Contains special character
```

### 3. Case Sensitive
Variable names are case-sensitive. `Name`, `name`, and `NAME` are three different variables.

#### Example:
```python
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)  # Prints: Alice
print(Name)  # Prints: Bob
print(NAME)  # Prints: Charlie
```

### 4. Cannot Use Python Keywords
Python has reserved keywords that cannot be used as variable names.

#### ❌ Invalid (Python Keywords):
```python
if = 5  # Syntax error
for = "loop"  # Syntax error
class = "MyClass"  # Syntax error
def = "function"  # Syntax error
import = "module"  # Syntax error
return = "value"  # Syntax error
while = True  # Syntax error
True = False  # Syntax error
None = 0  # Syntax error
```

#### Complete List of Keywords:
`False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`

---

## Best Practices (Naming Conventions)

These aren't hard restrictions, but they follow Python style guidelines (PEP 8) and make your code more professional and readable.

### 1. Use Lowercase with Underscores (snake_case)
- **Best practice** for variable and function names
- Makes code more readable and follows Python conventions

#### ✅ Recommended:
```python
user_name = "Alice"
first_name = "John"
total_score = 100
is_active = True
calculate_total_price()
get_user_data()
```

#### ❌ Not Recommended (but valid):
```python
userName = "Alice"  # camelCase - not Pythonic
UserName = "Bob"  # PascalCase - reserved for classes
USERNAME = "Charlie"  # UPPER_CASE - reserved for constants
username = "Dave"  # This is fine, but longer names benefit from underscores
```

### 2. Use Uppercase with Underscores for Constants
- Use for values that never change
- Signals to other developers that this shouldn't be modified

#### ✅ Recommended:
```python
MAX_ATTEMPTS = 3
DATABASE_URL = "postgresql://localhost/mydb"
PI_VALUE = 3.14159
DEFAULT_TIMEOUT = 30
```

#### ❌ Not Recommended:
```python
maxAttempts = 3  # Looks like a variable, not a constant
max_attempts = 3  # Looks like a variable, not a constant
```

### 3. Use PascalCase for Class Names
- First letter of each word is capitalized
- No underscores between words

#### ✅ Recommended:
```python
class User:
    pass

class CustomerAccount:
    pass

class DataProcessor:
    pass
```

#### ❌ Not Recommended:
```python
class user:  # Should be capitalized
    pass

class customer_account:  # Should be PascalCase
    pass
```

### 4. Use Meaningful, Descriptive Names
- Names should reflect what the variable contains
- Avoid single letters (except in loops or standard contexts)

#### ✅ Recommended:
```python
user_email = "john@example.com"
total_price = 99.99
is_logged_in = True
customer_list = []
```

#### ❌ Not Recommended:
```python
x = "john@example.com"  # Not descriptive
p = 99.99  # What does 'p' mean?
flag = True  # What is this flag for?
lst = []  # Too abbreviated
```

### 5. Use Single Letter Variables Only in Specific Cases
- Loop indices: `i`, `j`, `k`
- Mathematical formulas: `x`, `y`, `z`
- Exception handling: `e`

#### ✅ Recommended:
```python
for i in range(10):
    print(i)

try:
    dangerous_operation()
except Exception as e:
    print(f"Error: {e}")

# In math context
x = 5
y = 10
z = x + y
```

#### ❌ Not Recommended:
```python
u = "john@example.com"  # Should be user_email
p = [1, 2, 3]  # Should be prices or product_list
f = True  # Should be is_logged_in
```

### 6. Avoid Using Reserved Words as Part of Names
Even though you can't use them as variable names, it's confusing to use them in variable names.

#### ❌ Avoid:
```python
class_name = "Student"  # 'class' is a keyword
import_data = []  # 'import' is a keyword
return_value = 42  # 'return' is a keyword
```

#### ✅ Better:
```python
class_name = "Student"  # Actually acceptable if clear
data_to_import = []
result_value = 42
```

---

## Summary Table

| Category | Rule | Valid | Invalid |
|----------|------|-------|---------|
| **Start** | Letter/underscore only | `name`, `_var` | `2var`, `@var` |
| **Characters** | Alphanumeric + underscore | `user_name`, `id123` | `user-name`, `user@name` |
| **Case Sensitive** | Different cases = different vars | `name` ≠ `Name` | Can't reuse same name |
| **Keywords** | Cannot use Python keywords | `user_name` | `if`, `for`, `class` |
| **Convention** | Use snake_case for variables | `user_email` | `userName` |
| **Constants** | Use UPPER_CASE | `MAX_SIZE` | `max_size` |
| **Classes** | Use PascalCase | `UserAccount` | `user_account` |
| **Meaningful** | Use descriptive names | `total_price` | `x`, `temp` |

---

## Quick Reference

### Valid Variable Names ✅
```python
age = 25
user_name = "John"
_private = 42
count2024 = 100
is_valid = True
```

### Invalid Variable Names ❌
```python
2age = 25  # Starts with number
user-name = "John"  # Contains hyphen
user name = "John"  # Contains space
if = 5  # Python keyword
class = "test"  # Python keyword
@user = "John"  # Starts with special character
```
