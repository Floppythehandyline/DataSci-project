import numpy as np
ar = np.arange(0,20)
print(ar)
ar = np.split(ar,4)
print(ar,'\n')
br = np.array([[2,3,5,1],
               [7,11,13,2],
               [17,19,23,3]])
print(br,"\n")
h = np.hsplit(br,2)
print(h)
v = np.vsplit(br,3)
print(v)