"""
2. Write a python program to create a 2D array and perform the following operations  on it,
		a. print the dimension of the array
		b. update the array by changing the dimension to 3D
		c. add 5 to every element, subtract 2 from each element, multiply each element by 5
"""
import numpy as np
twod_array = np.ndarray((2,4),dtype=int)

print("\nDimension of the array is",twod_array.shape)
twod_array.fill(1)


print("Original Contents of the 2d array:",twod_array)


threed_array = twod_array.reshape((2,2,2))
print("\nDimension of the new array is",threed_array.shape)

print("Original Contents of the 3d array:",threed_array)

threed_array +=5
print("\nAfter Adding 5 to each element")
print(threed_array)

threed_array -=2
print("\nAfter Subtracting 2 from each element")
print(threed_array)

threed_array *=5
print("\nAfter Multiplying 5 to each element")
print(threed_array)