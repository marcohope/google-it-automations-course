# Variables: 

Represent data stored as strings, tuples, dictionaries, lists, and objects (note: future readings explain these categories)

#  Key Words

Special words that are reserved for specific purposes and that can only be used for those purposes

in
not
or
for
while
return

#  Operators

Symbols that perform operations on objects and values

+
- 
* 
/ 
** 
% 
// 
> 
< 
==

# Expressions: 

A combination of numbers, symbols, and variables to compute and return a result upon evaluation

# Functions:

 A group of related statements to perform a task and return a value

example:

def to_celsius(x):
   '''Convert Fahrenheit to Celsius'''
   return (x-32) * 5/9


to_celsius(75)

# Conditional statements: 

Sections of code that direct program execution based on specified conditions

example:

number = -4


if number > 0:
   print('Number is positive.')
elif number == 0:
   print('Number is zero.')
else:
   print('Number is negative.')

# Naming rules and conventions

When assigning names to objects, programmers adhere to a set of rules and conventions which help to standardize code and make it more accessible to everyone. Here are some naming rules and conventions that you should know:

Names cannot contain spaces.

Names may be a mixture of upper and lower case characters.

Names can’t start with a number but may contain numbers after the first character.

Variable names and function names should be written in snake_case, which means that all letters are lowercase and words are separated using an underscore. 

Descriptive names are better than cryptic abbreviations because they help other programmers (and you) read and interpret your code. For example, student_name is better than sn. It may feel excessive when you write it, but when you return to your code you’ll find it much easier to understand.