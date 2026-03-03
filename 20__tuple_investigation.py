from random import shuffle

t = (1,2,3,4,5)

print(t)
print(len(t))
print(t[0])
print(t[1:4])
print(t[::2])
print(t[::-1])

# Tuples are immutable, so we cannot change their values
# t[0] = 10 # This will raise a TypeError
# We can create a new tuple by concatenating two tuples

t2 = t + (6,7,8)

print(t2)

# We can also create a tuple from a list
l = [1,2,3,4,5]
t3 = tuple(l)
print(t3)

# We can also convert a tuple back to a list
l2 = list(t3)
print(l2)

# We can also use tuples to unpack values
a, b, c, d, e = t
print(a, b, c, d, e)

def process_tuple(t):
    a, b, c, d, e = t
    print(f"Processing tuple: {a}, {b}, {c}, {d}, {e}")

process_tuple(t)

l = [1,2,3,4,5,6,7,8,9,10]
shuffle(l)
print(l)

def process_list(l):
    mx = max(l)
    mn = min(l)
    return (mx, mn)


result = process_list(l)
print(result)
print(f"max = {result[0]}, min = {result[1]}")

(mx, mn) = process_list(l)
print(f"max = {mx}, min = {mn}")

# Swamping values using tuple unpacking
a = 10
b = 20
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

d = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "active": True
}

print(d.items())
print(type(d.items()))

for item in d.items():
    print(item)
    
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

#This is also a tuple, but it is not a single element tuple
t = (1,)
print(type(t))
