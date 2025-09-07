import numpy as n
a = n.arange(1,11)
print(a)
b = a[[1,3,5,7]]
print(b)

AA = n.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
BB = AA[[0,1],[2]]
print(BB)

print(a[a<5])
print(a[a>2])
print(a[a==3])