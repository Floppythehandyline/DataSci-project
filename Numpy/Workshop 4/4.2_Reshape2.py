import numpy as n
ar = n.arange(1,25)
print(ar,'\n')
B = n.reshape(ar,[6,-1])
print(B,'\n')
B = n.reshape(ar,[-1,8])
print(B,'\n')