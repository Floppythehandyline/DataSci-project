import pandas as p
#สร้าง series จาก list
Alist = [2,3,4,7,85,342]
sr1 = p.Series(data=Alist)
print(sr1,'\n')
#สร้าง series จาก tuple
Btuple = (5,7,7)
sr2 = p.Series(data=Btuple)
print(sr2,'\n')
#สารมารถสร้างได้ตรงๆ เลย
sr3 = p.Series([55,82,4,1,9])
print(sr3,'\n')
#สามารถใช้ range ได้
sr4 = p.Series(range(0,10,2))
print(sr4)