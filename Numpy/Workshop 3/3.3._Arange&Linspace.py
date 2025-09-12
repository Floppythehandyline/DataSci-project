import numpy as n
a = n.arange(1,5) #arange ใช้สร้าง array 1 มิติ โดยใส่ค่าที่กำหนด(ที่นี้คือ 1-4)
print(a,'\n')
b = n.arange(10,0,-2) #โดยจะเป็นในรูปแบบ arange(start,stop,step)
print(b,'\n')
c = n.arange(1,7,dtype=int) #สามารถกำหนดชนิดตัวแปรได้ด้วย dtype
print(c.astype('f'),'\n') #astype ใช้ในการแสดงค่าตัวแปร โดยสามารถกำหนดชนิดตัวแปรที่ต้องการจะแสดงได้

AA = n.linspace(1,4,6) #linspace ใช้ในการแบ่งค่าระหว่างกลาง รูปแบบจะเป็น linspace(start,stop,amount)   โดย amount คือ"จำนวน"ค่าที่อยู่ระหว่างกลาง ที่เราต้องการ
print(AA,'\n')
BB = n.linspace(1,4,12) #ถ้าไม่สามารถแบ่งลงตัวได้ ก็จะเป็นค่าทศนิยม
print(BB,'\n')
CC = n.linspace(6,1,12) #สามารถทำแบบ reverse ได้
print(CC,'\n')
DD = n.logspace(1,10,10,base=2) 
print(DD)