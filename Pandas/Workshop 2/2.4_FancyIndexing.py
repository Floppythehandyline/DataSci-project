import pandas as p

A = [11,22,33,44,55]
sr1 = p.Series(A,index=list("abcde"))
id = list('aabbc')
print(sr1[id])