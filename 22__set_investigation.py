# Data structures in python:
# 1. Lists
# 2. Tuples
# 3. Sets
# 4. Dictionaries

# List
names = ["alice", "bob", "charlie", "david", "eve", "alice", "bob"]
print(names)

#Set
names = {"alice", "bob", "charlie", "david", "eve", "alice", "bob"}
print(names)
names.add("frank")
print(names)
names.remove("alice")
print(names)

# A set is an unordered collection of unique elements. It does not allow duplicate values and does not maintain the order of elements. Sets are mutable, meaning you can add or remove elements from a set after it has been created.
# You can create an empty set using the set() function

empty_set = set()

# Uniquify two lists using a set
list1 = [1, 2, 3, 4, 5, 1, 2]
list2 = [4, 5, 6, 7, 8, 4, 5]

unique_elements = set(list1) | set(list2)
print(unique_elements)

unq_set = set(list1 + list2)
print(unq_set)

# Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B) # Union
print(A & B) # Intersection
print(A - B) # Difference
print(B - A) # Difference
print(A ^ B) # Symmetric Difference

