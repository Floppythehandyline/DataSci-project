import pandas as p
import numpy as n
#การใช้ร่วมกับ numpy เบื้องต้น
AA1 = n.arange(7,15)
sr = p.Series(AA1)
print(sr)

BB2 = n.random.randint(5,25,5)
sr2 = p.Series(BB2)
print(sr2)

CC3 = n.linspace(1,2,10)
sr3 = p.Series(CC3)
print(sr3)