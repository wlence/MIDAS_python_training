# 
message = "lorem ipsum dolor sit amet"

print(message.title())  # Output: "Lorem Ipsum Dolor Sit Amet"

a = 5
b = 3
result = a + b  # Output: 8

#You can't add a number to a string without converting the number to a string first
print("The result is " + str(result))  # Output: "The result is 8"

# Alternatively, you can use f-strings (Python 3.6+)
print(f"The result is {result}")  # Output: "The result is 8"

# \n is a newline character that creates a new line in the output
# \t is a tab character that creates a horizontal tab in the output
# \r is a carriage return character that moves the cursor to the beginning of the line
# \" is an escape character that allows you to include a double quote in a string
# \\ is an escape character that allows you to include a backslash in a string
# You can also use triple quotes (''' or """) to create multi-line strings

calculation = f"""
  {a} 
+ {b} 
-----
  {result}
"""
print(calculation)

message.split()  # Output: ['lorem', 'ipsum', 'dolor', 'sit', 'amet']


