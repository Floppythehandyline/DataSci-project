import pandas as p
import numpy as n

A = n.array([1,2,n.nan,4,n.nan,6])
sr = p.Series(A)
print(sr,'\n')
sr2 = p.Series(n.array([n.nan,1,1,2,5,n.nan]))
print(sr2,'\n')
print(sr+sr2,
      sr-sr2,
      sr*sr2,sep='\n')

print('\n',
      sr.sum(),
      sr.mean(),
      sr.count(),
      sr.size,
      sep='\n')
print('\n',
      sr.sum(skipna=False),
      sr.mean(skipna=False),sep='\n')