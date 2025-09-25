import pandas as p
import numpy as n

sr1 = p.Series([n.nan,2,3,n.nan,5],
               index=list('abcde'))
sr2 = sr1.dropna()      #จะ drop ค่าที่เป็น NaN
sr3 = sr1.fillna(-1)    #เปลี่ยนค่าที่เป็น NaN เป็นอย่างอื่น
print(sr2,
      sr3,
      sr1.hasnans,      #hasnans ตรวจสอบว่ามีค่าที่เป็น NaN รึไม่
      sr2.hasnans,
      sep=2*'\n')