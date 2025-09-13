import numpy as n
a = n.random.randint(0,10,5)
b = n.random.randint(11,21,5)

the = n.concatenate([a,b])
print(the)