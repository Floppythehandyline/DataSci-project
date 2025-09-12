import numpy as n
a = n.identity(4) #identity ใช้สร้าง array เอกลักษณ์(ในที่นี้คือ 4x4)
print(a,'\n')
b = n.identity(10,dtype='int') #สามารถกำหนดชนิดตัวแปรได้ด้วย dtype
print(b,'\n')

c = n.eye(2,4,k=1) #eye ใช้สำหรับเลื่อนตำแหน่งค่าใน array, k=1 หมายความว่า ให้เลื่อนไป 1
print(c)