import numpy as np
#slicing ของ list
list = [1,2,3,5,7,11]
print(list[1:5],'\n')
#slicing ของ array
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr[1,2],'\n')
print(arr[2][0:2],'\n')
print(arr[0:2,0:2],"\n")
print(arr[0:,2:])