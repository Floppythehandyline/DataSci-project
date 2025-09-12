import numpy as n
a = n.array([[1,2],[3,4],[5,6]])

b = a.flatten() #flatten จะแปลง array จากมิติใดๆ เป็น array 1 มิติ
a[0,0] = 6
print(a,'\n''\n',b)

c = a.ravel() #ravel จะคล้ายๆ กันกับ flatten แต่หาก array มีการเปลี่ยนแปลงค่า ravel ก็จะมีกาารอัปเดตด้วย
print('\n',c)