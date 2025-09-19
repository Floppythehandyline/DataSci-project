import pandas as p

A = [11,22,33,44,55]
sr1 = p.Series(A,index=[1,2,2,4,4])
print(sr1.loc[2:4])