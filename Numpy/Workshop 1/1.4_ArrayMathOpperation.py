import numpy as num
A = [5,8,6,9]
B = [7,8,2,1]
x = []

for i in range(4):
    ex = int(input(""))
    x.append(ex)
    
A = num.array(A)
B = num.array(B)
x = num.array(x)
print((A*x)+B)