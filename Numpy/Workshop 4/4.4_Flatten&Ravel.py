import numpy as n
a = n.array([[1,2],[3,4],[5,6]])

b = a.flatten()
a[0,0] = 6
print(a,'\n''\n',b)

c = a.ravel()
print('\n',c)