import pandas as p

A = [11,22,33,44,55]
sr1 = p.Series(A,index=list("abcde"))
print(sr1['a':'d']) #label index
print(sr1[2:5]) #position index