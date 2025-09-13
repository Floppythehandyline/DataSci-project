import numpy as np
ar = np.array([[2,3,5],
               [7,11,13],
               [17,19,21]])
print(np.sum(ar,axis=0))
print(np.sum(ar,axis=1),'\n')
print(np.prod(ar,axis=0))
print(np.prod(ar,axis=1),'\n')
print(np.min(ar,axis=0))
print(np.min(ar,axis=1),'\n')
print(np.max(ar,axis=0))
print(np.max(ar,axis=1),'\n')
print(np.mean(ar,axis=0))
print(np.mean(ar,axis=1),'\n')
print(np.argmin(ar,axis=0))         #จะบอก index ที่มีค่าน้อยที่สุด
print(np.argmin(ar,axis=1),'\n')
print(np.argmax(ar,axis=0))         #จะบอก index ที่มีค่ามากที่สุด
print(np.argmax(ar,axis=1))