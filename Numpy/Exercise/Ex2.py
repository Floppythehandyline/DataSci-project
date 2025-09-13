#โจทย์: ให้สร้าง array แล้ววนลูปรับค่าจาก user โดยจะหยุดเมื่อ user ใส่ค่า 0 ลงไป
import numpy as np
ar = np.array([],dtype='int')
while True:
    ok = int(input("Enter number: "))
    if ok == 0:
        break
    else:
        ar = np.append(ar,ok)
        print(ar)