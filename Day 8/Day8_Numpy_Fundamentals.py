import numpy as np

# Numpy Basics
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)

# Array Creation
arr0 = np.array(4)  # 0D
print("\n0D Array:\n", arr0)

arr1 = np.array([1, 2, 3, 4, 5])  # 1D
print("\n1D Array:\n", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D
print("\n2D Array:\n", arr2)

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D
print("\n3D Array:\n", arr3)

arr4 = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])  # 4D
print("\n4D Array:\n", arr4)

# Vectorization example
arr = np.random.randint(1, 100, size=5)
print("\nVectorized input:", arr)
print("Squared:", arr ** 2)

# Reshape
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print("\nReshaped:\n", reshaped)

# Stack
a = np.array([[1, 2]])
b = np.array([[3, 4]])
print("\nVertical Stack:\n", np.vstack((a, b)))
print("\nHorizontal Stack:\n", np.hstack((a, b)))

# Statistics
data = np.array([[10, 20, 30], [40, 50, 60]])
print("\nMean axis=0:", np.mean(data, axis=0))
print("Mean axis=1:", np.mean(data, axis=1))

# linspace + random
print("\nLinspace:", np.linspace(0, 3, 5))
print("Random:", np.random.rand(2, 2))

# Dimensions
a = np.array(42)
b = np.array([1, 2, 3])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[1, 2], [3, 4]]])

print("\nDimensions:", a.ndim, b.ndim, c.ndim, d.ndim)

# Shape
arr = np.array([1, 2, 3, 4])
print("Shape:", arr.shape)

# Indexing
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Indexing:", arr[0, 1])

# Slicing
arr = np.array([1, 2, 3, 4, 5])
print("Slice:", arr[1:4])

# arange + reshape
arr = np.arange(1, 17).reshape(4, 4)
print("\n4x4 array:\n", arr)

# Random distributions
print(np.random.uniform(20, 30, (2, 2)))
print(np.random.randint(10, 15, (3, 3)))

# Inspection
arr = np.array([[1, 2], [3, 4]])
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)

# Operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print("\nAdd:", a + b)
print("Multiply:", a * b)
print("Mean:", np.mean(a))

# Universal functions
arr = np.array([1, 4, 9])
print("\nSqrt:", np.sqrt(arr))

arr = np.array([0, np.pi / 2])
print("Sin:", np.sin(arr))

arr = np.array([1, 2])
print("Exp:", np.exp(arr))

# Floor / Ceil / Round
arr = np.array([1.2, 2.8, -3.7])
print("\nFloor:", np.floor(arr))
print("Ceil:", np.ceil(arr))
print("Trunc:", np.trunc(arr))
print("Round:", np.round(arr))

# Log
arr = np.array([1, np.e, np.e**2])
print("\nLog:", np.log(arr))
