def greet(name, greeting="Hello", times=1):
    for _ in range(times):
        print(f"{greeting}, {name}!")

print(__name__)  # Output: __main__, or module name in other scripts

# This block will only execute if this script is run directly, not when imported as a module
if __name__ == "__main__":
    greet("Alice")  # Output: Hello, Alice!
    greet("Bob", greeting="Hi")  # Output: Hi, Bob!
    greet("Charlie", times=3)  # Output: Hello, Charlie! (printed 3 times)



