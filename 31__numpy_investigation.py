import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(arr)

# Create a 1D array of integers from 0 to 9
arr1d = np.arange(10)
print("1D Array:")
print(arr1d)

#Create a 2D array of shape (3, 4) filled with random integers between 0 and 9
arr2d = np.random.randint(0, 10, size=(3, 4))
print("2D Array:")
print(arr2d)

# Matrix operations
m1 = np.random.randint(0, 10, size=(2, 3))
m2 = np.random.randint(0, 10, size=(2, 3))

print("Matrix 1:")
print(m1)
print("Matrix 2:")
print(m2)
print("Element-wise Sum:")
print(m1 + m2)
print("Element-wise Product:")
print(m1 * m2)
print("Matrix Product:")
print(m1 @ m2.T)

print("Shape of Matrix 1:")
print(m1.shape)

# Extra slicing examples
print("First row of Matrix 1:")
print(m1[0])
print("Last column of Matrix 1:")
print(m1[:, -1])
print("Submatrix of Matrix 1 (first 2 rows and first 2 columns):")
print(m1[:2, :2])

