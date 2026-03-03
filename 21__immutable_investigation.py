numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers)

cp = numbers # This creates a new reference to the same list, not a copy of the list
print(cp)


numbers[0] = 99
print(numbers)
print(cp) # This will also show the change because cp is referencing the same list as numbers

cp = numbers[:] # This creates a new list that is a copy of the original list
print(cp)

numbers[0] = 1
print(numbers)
print(cp) # This will not show the change because cp is a different list than numbers

print(id(numbers)) # This will show the memory address of the numbers list
print(id(cp)) # This will show the memory address of the cp list, which is different from numbers

# Strings are also immutable, so when we change a string, we are actually creating a new string
s = "Hello"
print(s)
s = s + " World"
print(s)

print(id(s)) # This will show the memory address of the new string, which is different from the original string

