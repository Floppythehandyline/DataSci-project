#โจทย์: สร้าง array โดยใช้ linspace ค่า 0-1 จากนั้นให้เปลี่ยนเป็น array ขนาด 5x4
import numpy as np
ar = np.linspace(0,1,20)
print(ar)
test = np.reshape(ar,[5,4])
print(test)
print(test.shape)