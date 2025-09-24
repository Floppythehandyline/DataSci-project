import pandas as p
import numpy as n

def test(x):
    return 'ok' if x < 0 else x #short if

a = p.Series(n.random.randint(-11,11,5))
b = a.apply(test)
print(b)