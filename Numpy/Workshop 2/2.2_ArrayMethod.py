import numpy as np

A = np.zeros((2,3)) #สร้าง array 2x3 เติมด้วยเลข 0
print(A,"\n")

B = np.ones((4,3),dtype=int) #สร้าง array 4x3 เติมด้วยเลข 1 และกำหนดชนิดตัวแปรเป็น int
print(B,"\n")

C = np.full((5,5),7) #สร้าง array 5x5 เติมด้วยเลขที่กำหนดให้(7)
print(C,"\n")

D = np.full((3,3),True,dtype=bool) #สร้าง array เติมด้วย boolean
print(D)