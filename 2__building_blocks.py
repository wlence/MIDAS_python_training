# Building block #1 - Comment

# Building block #2 - Variables
x = 10
name = "Willian"
f = 3.14

# python is weakly typed, so we can reassign variables to different types
x = "Now I'm a string"

# Building block #3 - Expressions
a = 5
b = 3
sum = a + b
product = a * b
division = a / b

# Order of precedence is PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction)
result = (a + b) * 2 - 4 / 2

# Shortcut
# <alt> + <shift> + <up/down> to duplicate lines
# <alt> + <up/down> to move lines up or down

# Building block #4 - Loops
for i in range(5):
    print(f"Iteration {i}")

x = 0
while x < 20:
    print(f"x is {x}")
    x += 1

# Building block #5 - Conditional statements
age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a minor.")

# Inline conditional expression (ternary operator)
status = "adult" if age >= 18 else "minor"

#Building block #6 - Functions
# Built-in function: https://docs.python.org/3/library/functions.html
# Python standard library: https://docs.python.org/3/library/index.html
# Third-party libraries: https://pypi.org/

# Creating new functions
# Define a function to calculate the area of a circle
def area_of_circle(radius):
    return f * radius ** 2

area = area_of_circle(5)
print("The area of the circle is {}".format(area))

# Building block #7 - Lists/Arrays
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing the first element
my_list.append(6)  # Adding an element to the end of the list
for item in my_list:  # Iterating through the list
    print(item)

#Building block #8 - Objects
message = "this is a string"
print(message.upper())  # Calling a method on the string object
print(message.title())  # Calling another method on the string object


