import numpy as np
ar = np.arange(0,20)
print(ar)
ar = np.delete(ar,10)
print(ar,'\n')
#ลบ
br = np.array([[2,3,5],
               [7,11,13],
               [17,19,23]])
print(br,"\n")
br = np.delete(br,0,axis=0)
print(br)
br = np.delete(br,2,axis=1)
print(br)