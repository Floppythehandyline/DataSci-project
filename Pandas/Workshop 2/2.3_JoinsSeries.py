import pandas as p

A = [11,22,33,44,55]
sr1 = p.Series(A,index=list("abcde"))
sr2 = p.Series(A,index=list("abcde"))
print(sr1+10)
print(sr1-5)
print(sr1*2)
print(sr1**3)
print(sr1/10)
print(sr1+sr2)
print(sr1-sr2)