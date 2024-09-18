#Return array of odd and even from the numpy array
#NumPy (Numerical Python) is similar as lists but it is a lot more faster and efficient

import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8], [22,54,67,88], [12,13,11,17]])

odd_row_even_column = arr[::2, 1::2]

print("Original array: ")
print(arr)

print("Modified array: ")
print(odd_row_even_column)