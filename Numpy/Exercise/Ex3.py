import numpy as n
ar = n.arange(1,100)

# for i in range(len(ar)):
#     if ar[i] % 2 == 0 and ar[i] % 3 !=0:
#         print(ar[i])

print(ar[(ar%2==0)&(ar%3!=0)])