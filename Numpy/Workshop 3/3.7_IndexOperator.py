import numpy as n
a = n.arange(1,11)
print(a)
b = a[[1,3,5,7]]
print(b)

AA = n.array([[1,2,3],
              [4,5,6],
              [7,8,9]]) #เราสามารถเลือกค่าใน array แบบเจาะจงได้ โดยการใช้ index 
BB = AA[[0,1],[2]] #อันนี้หมายถึงเลือกค่าที่ row 0 ถึง 1, colum ที่ 2
print(BB)

print(a[a<5]) #แสดงค่าใน array a ที่ น้อยว่า 5
print(a[a>2]) #แสดงค่าใน array a ที่ มากกว่า 2
print(a[a==3]) #แสดงค่าใน array a ที่ เท่ากับ 3