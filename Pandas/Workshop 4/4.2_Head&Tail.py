import pandas as  p
import numpy as n

sr = p.Series(n.random.randint(10,100,10))
print(sr,
      sr.head(4),       
      sr.tail(4),
      sep=2*"\n")