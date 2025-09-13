import numpy as np
ar = np.arange(0,10)
print(ar)
ar = np.insert(ar,4,21)
print(ar)
ar = np.insert(ar,(3,7),777)
print(ar,'\n')

br = np.array([[2,3,5],
               [7,11,13]])
print(br,"\n")
br = np.insert(br,2,(15,17,19),axis=0)
print(br,"\n")
br = np.insert(br,3,(23,29,31),axis=1)
print(br,"\n")