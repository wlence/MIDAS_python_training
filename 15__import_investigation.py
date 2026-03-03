# Import individual functions from the random module
from random import randint, shuffle

r = randint(1, 10)

print(r)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(l)

print(l)

# import the entire random module
import random

r = random.randint(1, 10)
print(r)

random.shuffle(l)

print(l)

# import the entire random module with an alias
import random as rnd

r = rnd.randint(1, 10)
print(r)

rnd.shuffle(l)

print(l)

# Popular modules and aliases
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt


# import all functions from the random module (not recommended)
from random import *

r = randint(1, 10)
print(r)

shuffle(l)

print(l)

