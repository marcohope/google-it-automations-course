
#implicit conversion - automatic conversion of one data type to another
# print(7+5.5)

# print("a"+"b"+"c")

# print("This" + " " + "cat" + " " + "is" + " " + "in" + " " + "the" + " " + "tree")

# explicit conversion - manually converting one data type to another

# base = 6 
# height = 3 
# area = (base * height) / 2
# print("The area of the triangle is " + str(area))

#str() - converts a value to a string
# int() - converts a value to an integer
# float() - converts a value to a floating point number


# In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. 
# Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. 
# Finally, output a message saying "The average size is: " followed by the resulting number. 
# Remember to use the str() function to convert the number into a string. 

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The Average size is " + str(average))


