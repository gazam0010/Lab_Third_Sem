#Sort by second row & sort by column

import numpy as np
   
arr = np.array([[1,21,31,4], 
                [4,2,9,0], 
                [43,76,9,98], 
                [12,54,34,64]])
a = np.argsort(arr[1, :], kind='heapsort')

b = np.argsort(arr[:, 1])
a = [0,1,3,2]

print(arr[:,a])
