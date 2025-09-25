import pandas as p

sr = p.Series([10,20,30,40,40],index=list('abcde'))
sr2 = sr.map({10:101,40:400})
print(sr2)