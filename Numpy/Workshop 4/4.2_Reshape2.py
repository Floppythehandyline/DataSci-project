import numpy as n
ar = n.arange(1,25)
print(ar,'\n')
B = n.reshape(ar,[6,-1]) #ถ้าไม่ทราบว่าจำนวนแถวหรือหลักจะต้องมีเท่าไหร่ สามารถใส่เป็น -1 ไปได้
print(B,'\n')
B = n.reshape(ar,[-1,8]) #อย่าหาใส่ -1,-1 มันจะ error
print(B,'\n')