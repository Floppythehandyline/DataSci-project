import pandas as p
import numpy as n

A = p.Series(n.random.randint(0,10,5),index=list('abcde'))
sr1 = A.sort_values(ascending=True)     #เรียงค่าจาก น้อย ไป มาก
sr2 = A.sort_values(ascending=False)    #เรียงค่าจาก มาก ไป น้อย
sr3 = A.sort_values()                   #by default the ascending will be true
print(sr1,sr2,sr3,sep=2*'\n')