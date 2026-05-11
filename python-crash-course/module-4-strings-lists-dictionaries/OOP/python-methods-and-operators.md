# Python Methods and Special Operators

In Python, methods are behaviors associated with object parameters that modify the state of that object. They are essentially functions that belong to a specific instance of a class. This means that calling a method on a list, for example, only modifies that instance of the list, and not all lists globally.

Methods in Python fall into several categories:

- Instance methods
- Class methods
- Static methods

## Instance methods

Instance methods are the most common type of methods in Python. You define instance methods within a class by creating functions inside the class definition. When you instantiate instances of a class, those individual instances can have their methods called so the program can control and modify those instances directly. Instance methods can take a parameter called `self`, which represents the instance the method is being executed on, that allows you to access attributes of the instance using dot notation, like `self.name`, which will access the `name` attribute of that specific instance of the class object. When you have variables that contain different values for different instances, these are called instance variables.

## Class methods

Class methods, on the other hand, are called for the class itself instead of an instance. They are marked with a `@classmethod` decorator and take a `cls` parameter that points to the class—and not any specific instance—when the method is called. One common use-case for class methods is to create and modify data structures that contain records for all instances of a class. Usually, programmers make a list inside the class definition, and methods to add instances of the class to that list in order to keep track of that class.

## Static methods

Lastly, static methods, marked with a `@staticmethod` decorator, do not take a `self` or a `cls` parameter. Static methods behave like plain functions, except that you can call them directly from the class. It is important to note that you do not have to actually instantiate the class, the methods just reside in there. This is because class definitions are themselves an object (i.e., an instance of abstract base class), which reduces overhead and allows functions to be encapsulated in an easy-to-use encapsulation. Programmers use static methods when the method does not need to access any instance or class-specific data.

## Choosing a method type

The type of method you choose to use—instance, class, or static—depends on what data the method needs to access. Think of these methods as different tools in your toolbox, each with a different use-case depending on the data you need to work with.

- **Instance methods** are for individual object data
- **Class methods** for shared data
- **Static methods** for related tasks that don't need to access or modify any object or class data

## Key takeaways (methods)

Remember, methods in Python are a way to bundle behavior with objects, allowing you to interact with and modify the state of those objects. However, static methods offer a way to bundle functions together, to be used in general on any other type of object. Bundling functions together helps organize functions in a clean manner and helps package them for reuse in other coding projects.

## Constructors and special methods

Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a **constructor**. Below is an example of an `Apple` class with a constructor method defined.

```python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
```

When you call the name of a class, the constructor of that class is called. This constructor method is always named `__init__`. You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the `self` variable, which represents the instance, as well as `color` and `flavor` parameters. These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the `Apple` class and set the color and flavor values all in one go:

```python
jonagold = Apple("red", "sweet")
print(jonagold.color)
```

In addition to the `__init__` constructor special method, there is also the `__str__` special method. This method allows us to define how an instance of an object will be printed when it's passed to the `print()` function. If an object doesn't have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our `Apple` class, with the `__str__` method added:

```python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
```

Now, when we pass an `Apple` object to the print function, we get a nice formatted string:

```python
jonagold = Apple("red", "sweet")
print(jonagold)
```

```
This apple is red and its flavor is sweet
```

It's good practice to think about how your class might be used and to define a `__str__` method when creating objects that you may want to print later.

## Special operators

You have already learned about methods and how they are just functions that belong to a class. They define the behavior that an object of the class can perform. Special operators are specific symbols or keywords that are built-in and provide special behavior when used with certain data types or objects. In your class, you can define methods to implement or override the standard behavior of Python operators, thus creating methods as special operators.

### Different types of special operators

Python supports a variety of different operators that you can use in your code to make life easier for you. Some of the more common operators are:

- **Arithmetic operators.** These include `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), and `**` (exponentiation).
- **Comparison operators.** These include `==` (equality), `!=` (inequality), `<` (less than), and `>=` (greater than or equal to).
- **Logical operators.** These include `and`, `or`, and `not`.
- **Assignment operators.** These include `=` (simple assignment), `+=` (addition assignment), and `%=` (modulo assignment).

> Note: This is not an all-inclusive list, but different examples of common operators that you would use in Python.

### Performing special operations

Every special operator has a corresponding dunder method that implements the operation. In Python, you denote a dunder method by placing double underscores at the beginning and end of the name; in fact, the term "dunder" comes from this use of double underscores. You can change how an operator behaves with an instance of your object by overriding the implementation. Let's look at an example:

```python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
```

In this example, the `Triangle` class has a method `__init__()` which is called a constructor and is used to initialize the object's attributes.

```python
    def area(self):
        return 0.5 * self.base * self.height
```

This part of the code, `area(self)` method, computes the area of the triangle based on its height and base length.

```python
    def __add__(self, other):
        return self.area() + other.area()
```

This method overrides the `+` operator to "add" two triangles together.

```python
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
```

The output of this program is:

```
The area of triangle 1 is 25.0
The area of triangle 2 is 24.0
The area of both triangles is 49.0
```

Putting it all together, this is what the code should look like:

```python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __add__(self, other):
        return self.area() + other.area()


triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
```

For a full list of operators and the method names you can use to override their behavior, view this resource: **Mapping operators to functions**.

### Key takeaways (special operators)

Python allows you to override or implement standard operations in your code to make your code cleaner for yourself and others to read. Being able to override certain behaviors allows you to control the output of your code and provides flexibility in how you write code.

## Classes and methods cheat sheet

### Defining classes and methods

```python
class ClassName:
    def method_name(self, other_parameters):
        body_of_method
```

### Classes and instances

- Classes define the behavior of all instances of a specific class. In Python, the code defining a class is, itself, an object; classes can be used without instantiating a single object, such as when using static methods.
- Remember, each variable of a specific class is an instance or object.
- In Python, "getters and setters" are methods used for controlling access to an object's attributes. The getter method retrieves the value of an attribute, while the setter method sets or changes the attribute's value, often including some sort of validation or modification to the data before setting the value.
- You can access an instance's attribute, like `name`, by calling `self.name` within the class methods, or `<instance>.name` outside the class, where `<instance>` is the specific instance of the class you're working with.
- Objects can have attributes, which store information about the object.
- You can make objects do work by calling their methods.
- The first parameter of the methods, `self`, represents the current instance.
- Methods are just like functions, but they can only be used through a class.
- You can use class methods in conjunction with a class variable to track the number of instances of a class, incrementing the class variable each time an instance is created in the class's `__init__` method.

### Special methods

- Special methods start and end with `__`.
- Special methods have specific names, like `__init__` for the constructor or `__str__` for the conversion to string.
- The methods `__str__` and `__repr__` allow you to define human-readable and unambiguous string representations of your objects, respectively.
- By defining methods like `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, and `__ge__`, you can control how objects of your class are compared.

### Documenting classes, methods, and functions

You can add documentation to classes, methods, and functions by using **docstrings** right after the definition. Like this:

```python
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method


def function_name(parameters):
    """Documentation for the function."""
    body_of_function
```

A great way to use docstrings is to have an example of using the function, with its expected output.

```python
def my_function(x):
    """
    Sample usage:
    >>> my_function("example input")
    "example output"
    """
```

When in an interactive Python session, you can display docstrings with:

```python
help(some_function)
```

Or in your code you can retrieve it and use it in your program just as you would with any other string:

```python
print(some_function.__doc__)
```
