def greet(name, greeting="Welcome", times=1):
    for i in range(times):
        print(f"{greeting} {name}!")

greet("Alice", "Hello")  # Output: Hello, Alice!
greet(name="Bob", greeting="Hi")  # Output: Hi, Bob!
greet("Charlie")  # Output: Welcome, Charlie!

greet("Dave", times=3)



