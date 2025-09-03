import numpy as nu
array1 = nu.array([1,2,3,4])
array2 = nu.array((9,8,4,6))

print(type(array1))
print(type(array2))

for i in range(len(array1)):
    print(array1[i] + array2[i])

print(array1 + array2)