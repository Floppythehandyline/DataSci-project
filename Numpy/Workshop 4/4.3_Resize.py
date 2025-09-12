import numpy as n
ar = n.arange(0,10)
a = n.reshape(ar,[2,5])
b = n.resize(ar,[2,5])  #คล้ายกับ reshape แต่มันจะไม่อัปเดตหาก array มีการเปลี่ยนแปลง
ar[0] = 6
print(a,'\n')
print(b)