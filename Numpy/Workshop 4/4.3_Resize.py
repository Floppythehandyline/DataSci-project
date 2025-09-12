import numpy as n
ar = n.arange(0,10)
a = n.reshape(ar,[2,5])
b = n.resize(ar,[2,5])
ar[0] = 6
print(a,'\n')
print(b)