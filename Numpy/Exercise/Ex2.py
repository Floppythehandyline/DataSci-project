#โจทย์: 
import numpy as np
ar = np.array([],dtype='int')
while True:
    ok = int(input("Enter number: "))
    if ok == 0:
        break
    else:
        ar = np.append(ar,ok)
        print(ar)