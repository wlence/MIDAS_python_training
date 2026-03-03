#Python is good at handling big numbers. You can do math with them and they will be accurate. In some languages, you have to use special libraries to handle big numbers, but in Python, it's built-in.

n = 546845616644556464651684654316843515464
n2 = 46661646354165168164651616423516464165165

print(n*n2)

# Not so good at small numbers. If you try to do math with very small numbers, you might get a result that is not accurate because of the way computers handle floating point numbers.
a = 0.1
b = 0.2
print(a + b) # This will not give you 0.3 because of the way floating point numbers are represented in computers

#Libraries for handling small numbers
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b) # This will give you 0.3 because the Decimal library is designed to handle small numbers accurately

#Binary numbers are also handled well in Python. You can use the built-in bin() function to convert a number to binary and the int() function to convert a binary string back to an integer.
a = 0b1011
b = 0b1101

print(a + b) # This will give you 0b11000 because the sum of 0b1011 and 0b1101 is 0b11000

# You can also convert a binary number to a decimal number using the int() function.
a = 0b1011
b = 0b1101
print(int(a)) # This will give you 11 because 0b1011 is 11 in decimal
print(int(b)) # This will give you 13 because 0b1101 is 13 in decimal  

#bitwise operations are also supported in Python. You can use the & operator for bitwise AND, the | operator for bitwise OR, the ^ operator for bitwise XOR, and the ~ operator for bitwise NOT.
a = 0b1011
b = 0b1101
print(a & b) # This will give you 0b1001 because the bitwise AND of 0b1011 and 0b1101 is 0b1001
print(a | b) # This will give you 0b1111 because the bitwise OR of 0b1011 and 0b1101 is 0b1111
print(a ^ b) # This will give you 0b0110 because the bitwise XOR of 0b1011 and 0b1101 is 0b0110
print(~a) # This will give you -0b1100 because the bitwise NOT of 0b1011 is -0b1100 (in two's complement representation)
#shift operators are also supported in Python. You can use the << operator for left shift and the >> operator for right shift.
a = 0b1011
print(a << 2) # This will give you 0b101100 because the left shift of 0b1011 by 2 is 0b101100
print(a >> 2) # This will give you 0b10 because the right shift of 0b1011 by 2 is 0b10

#hexadecimal numbers are also supported in Python. You can use the built-in hex() function to convert a number to hexadecimal and the int() function to convert a hexadecimal string back to an integer.
a = 0x1A
b = 0x2F

print(a + b) # This will give you 0x49 because the sum of 0x1A and 0x2F is 0x49
print(int(a)) # This will give you 26 because 0x1A is 26 in decimal

#Octal numbers are also supported in Python. You can use the built-in oct() function to convert a number to octal and the int() function to convert an octal string back to an integer.
a = 0o17

value = "0xffed"
n = int(value, base=16) # This will convert the hexadecimal string to an integer
print(n) # This will give you 65517 because 0xffed is 65517 in decimal

