# Generate random numbers and perform basic operations
import random
# Generate a random integer between 1 and 100
random_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_int}")

print(f"{random_int} is {'small' if random_int < 20 else 'medium' if random_int < 50 else 'large' if random_int < 80 else 'very large'}")
# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")
# Generate a random number from a normal distribution with mean 0 and standard deviation 1
random_normal = random.gauss(0, 1)
print(f"Random number from normal distribution (mean=0, std=1): {random_normal}")
# Generate a random number from a uniform distribution between 0 and 10
random_uniform = random.uniform(0, 10)
print(f"Random number from uniform distribution between 0 and 10: {random_uniform}")

