import pandas as p

sr1 = p.Series([1,2,3,4,5],index=list('abcde'))
sr2 = sr1.rename({'a':'hey',"d":'hi'})          #เปลี่ยนชื่อ index ทีละตัว
print(sr2,'\n')
sr2.index = ['hello','hi','hey','howdy','ola']  #เปลี่ยนยกชุด
print(sr2)