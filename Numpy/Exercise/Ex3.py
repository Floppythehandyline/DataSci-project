#โจทย์: ให้ใช้ arange สร้าง array เก็บค่า 1-100 แล้วให้นำค่ามาแสดงผล
#โดยมีเงื่อนไขว่า จะต้องหารด้วย 2 ลงตัว แต่ต้องหาร 3 ไม่ลงตัว
import numpy as n
ar = n.arange(1,100)

#วิธีคิดแบบใช้ for loop
# for i in range(len(ar)):
#     if ar[i] % 2 == 0 and ar[i] % 3 !=0:
#         print(ar[i])

print(ar[(ar%2==0)&(ar%3!=0)])