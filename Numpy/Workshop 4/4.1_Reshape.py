import numpy as np
ar = np.arange(0,10)
print(ar,'\n')
test = np.reshape(ar,[2,5])
print(test,'\n')
test = np.reshape(ar,[1,10])
print(test,'\n')
test = np.reshape(ar,10)
print(test,'\n')