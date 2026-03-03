# A dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure in Python. Dictionaries are defined using curly braces {} and consist of key-value pairs separated by colons (:). Each key must be unique, and the values can be of any data type.
d = {
    "id": 1, 
    "name": "Alice", 
    "age": 30, 
    "email": "alice@example.com", 
    "active": True 
}

print(d)  # Output: {'id': 1, 'name': 'Alice', 'age': 30, 'email': '
# Accessing values in a dictionary
print(d["name"])  # Output: "Alice"
print(d["age"])   # Output: 30

# Modifying values in a dictionary
d["age"] = 31

# Adding new key-value pairs to a dictionary
d["country"] = "USA"

# Removing key-value pairs from a dictionary
del d["email"]

# Dictionary methods
print(d.keys())    # Output: dict_keys(['id', 'name', 'age', 'active', 'country'])
print(d.values())  # Output: dict_values([1, 'Alice', 31, True, 'USA'])
print(d.items())   # Output: dict_items([('id', 1), ('name', 'Alice'), ('age', 31), ('active', True), ('country', 'USA')])

# Checking if a key exists in a dictionary
print("name" in d)  # Output: True
print("email" in d)  # Output: False

# Iterating over a dictionary
for key, value in d.items():
    print(f"{key}: {value}")

# get() method to access values in a dictionary
print(d.get("name"))  # Output: "Alice"
print(d.get("email", "Not found"))  # Output: "Not found"

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
print(squared)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#d.copy()  # Create a shallow copy of the dictionary
#d.clear()  # Clear all key-value pairs from the dictionary

d.keys()  # Output: dict_keys(['id', 'name', 'age', 'active', 'country'])
d.values()  # Output: dict_values([1, 'Alice', 31, True, 'USA'])
d.items()  # Output: dict_items([('id', 1), ('name', 'Alice'), ('age', 31), ('active', True), ('country', 'USA')])



