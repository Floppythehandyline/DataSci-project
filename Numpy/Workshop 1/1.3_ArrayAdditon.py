import numpy as nu
array1 = nu.array([1,2,3,4]) #ตัวแปร list
array2 = nu.array((9,8,4,6)) #ตัวแปร tuple
#ตรวจสอบชนิดตัวแปร
print(type(array1))
print(type(array2))
#วนลูปบวกค่าโดย for loop
for i in range(len(array1)):
    print(array1[i] + array2[i])

#numpy สามารถเขียนอย่างงี้ได้เลย
print(array1 + array2)