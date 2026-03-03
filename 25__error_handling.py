from random import randint

a = 10
b = 0
numbers = [1, 2, 3, 4, 5]
value = "ten"

r = randint(1, 4) # This will raise a NameError because randint is not defined

try:
    if r == 1:
        answer = a / b # This will raise a ZeroDivisionError
    elif r == 2:
        answer = numbers[10] # This will raise an IndexError
    elif r == 3:
        answer = int("ten") # This will raise a ValueError
    else:
        answer = "No error"
except ZeroDivisionError:
    print("Cannot divide by zero")
    answer = 0
except IndexError:
    print("List index out of range")
    answer = numbers[-1]
#Catch all other exceptions
except Exception as e:
    print(f"An error occurred: {e}")
    answer = -1
finally:
    print("This will always be executed")

print(f"The answer is: {answer}")

#ZeroDivisionError: division by zero
division = a / b # This will raise a ZeroDivisionError

#IndexError: list index out of range
print(numbers[10]) # This will raise an IndexError

#ValueError: invalid literal for int() with base 10: 'ten'
number = int(value) # This will raise a ValueError
