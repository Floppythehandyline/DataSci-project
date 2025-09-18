import pandas as p
#เปลี่ยนเลข index ที่แสดงด้านหน้า
da = [1,2,3,4,5]
idx = ['iphone','huawei','samsung','nokia','pixel']
sr = p.Series(da,index=idx)
print(sr,'\n')

sr2 = p.Series([22,33,44],index=["bule","red","green"])
print(sr2,'\n')

sr3 = p.Series(da,index=list("abcde"))
print(sr3)