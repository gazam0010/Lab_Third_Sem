#Sort by second row & sort by column
#argsort stores the sorted indices of the selected row/column

import numpy as np

def sort_by_row(arr):
    a = np.argsort(arr[1, :])
    return arr[:, a]

def sort_by_column(arr):
    a = np.argsort(arr[:, 1])
    return arr[a, :]
   
arr = np.array([[1,21,31,4], [4,2,9,0], [43,76,9,98], [12,54,34,64]])

choice = int(input("Enter choice: 1 for row and 2 for cloumn: "))

print("Original array: ")
print(arr)
print("\n Sorted array: ")

if choice == 1:
    print(sort_by_row(arr))
else:
    print(sort_by_column(arr))