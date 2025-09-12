import numpy as np
ar = np.arange(0,10)
print(ar,'\n')
test = np.reshape(ar,[2,5]) #reshape ใช้แปลง array
print(test,'\n')            #reshape(array,[ขนาดที่ต้องการ])
test = np.reshape(ar,[1,10])
print(test,'\n')
test = np.reshape(ar,10)    #ด้านบนมันจะเป็น 2 มิติ ถ้าอยากได้ 1 มิติ ก็พิมพ์อย่างนี้
print(test,'\n')