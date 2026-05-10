fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
# adds "Kiwi" to the end of the fruits list
print(fruits)

fruits.insert(0, "Orange")
# takes an index as the first paramenter and an element as the second parameter then adds the element at the index
print(fruits)

fruits.remove("Pineapple")
print(fruits)

fruits.pop(3)
#removes element at index passed; in this case Melon
print(fruits)

fruits[2] = "Strawberry"
#replaced the index with the element. So Apple with Strawberry 
print(fruits)