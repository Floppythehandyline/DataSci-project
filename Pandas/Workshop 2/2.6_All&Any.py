import pandas as p
import numpy as n

AA = n.random.randint(1,11,5)
sr = p.Series(AA)
print(sr,
      (sr>5).all(),
      (sr % 2 == 0).any())