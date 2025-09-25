import pandas as p

sr = p.Series([1,2,3,4,5],index=list('abcde'))
sr2 = sr.drop('b')
sr3 = sr.drop({'c','d'})
print(sr2,sr3,sep=2*'\n')