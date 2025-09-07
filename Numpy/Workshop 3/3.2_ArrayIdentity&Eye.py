import numpy as n
a = n.identity(4)
print(a,'\n')
b = n.identity(10,dtype='int')
print(b,'\n')

c = n.eye(2,4,k=1)
print(c)