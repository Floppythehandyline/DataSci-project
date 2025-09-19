import pandas as p

A = [11,22,33,44,55]
sr1 = p.Series(A)

print('count: ',sr1.count())
print('mean: ',sr1.mean())
print('std: ',sr1.std())
print('max: ',sr1.max())
print('min: ',sr1.min(),'\n')

print(sr1.describe())