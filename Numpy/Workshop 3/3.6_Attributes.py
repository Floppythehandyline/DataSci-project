import numpy as n
a = n.full((5,5),7)
print(a.shape) #แสดงรูปร่าง(shape)ของ array
print(a.dtype) #แสดงชนิดตัวแปรใน array
print(a.ndim) #แสดงมิติของ array
print(a.size) #แสดงจำนวนข้อมูลที่อยู่ใน array
print(a.itemsize) #แสงขนาดของข้อมูลใน array (หน่วยเป็น byte)