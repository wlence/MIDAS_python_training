# Lists in Python
# A list is a collection of items in a particular order
# Lists are mutable, meaning their elements can be changed
# Lists are defined using square brackets []

# Example of a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ["apple", "banana", "cherry"]

# Accessing elements in a list
print(fruits[0])  # Output: "apple"
print(fruits[1])  # Output: "banana"
print(fruits[2])  # Output: "cherry"

# Modifying elements in a list
fruits[0] = "orange"
print(fruits)  # Output: ["orange", "banana", "cherry"]

# Adding elements to a list
fruits.append("grape")
print(fruits)  # Output: ["orange", "banana", "cherry", "grape"]

# Removing elements from a list
fruits.remove("banana")
print(fruits)  # Output: ["orange", "cherry", "grape"]

# List slicing
print(fruits[0:2])  # Output: ["orange", "cherry"]
print(fruits[:2])   # Output: ["orange", "cherry"]
print(fruits[1:])   # Output: ["cherry", "grape"]

# List length
print(len(fruits))  # Output: 3

# Negative indexing
print(fruits[-1])  # Output: "grape"
print(fruits[-2])  # Output: "cherry"

# List item detection
print("orange" in fruits)  # Output: True
print("banana" in fruits)  # Output: False


