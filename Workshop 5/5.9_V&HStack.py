import numpy as n
a = n.random.randint(0,10,(3,3))
b = n.random.randint(11,21,(3,3))
print(a,'\n\n',b,'\n')

v = n.vstack([a,b])
print(v,'\n')
h = n.hstack([a,b])
print(h)