#ให้สร้าง OOP ของรถให้กำหนดชนิด สีรถ ยี้ห้อ ความเร็ว และคืนค่า(return)ชนิด สีรถ ยี้ห้อ ความเร็ว ให้สร้างรถ 3 คัน

class automoblie:
    type = ""
    color = "" 
    brand = ""
    speed = ''
    def forward(self,fw):
        return 'forward '+str(fw)+' meters'

A = automoblie()
A.type = "sedan" 
A.color = "white"
A.brand = "Ford"
A.speed = "100kph"
print(A.type,A.color,A.brand,A.speed)
print(A.forward(150),'\n')

car = automoblie()
car.type = "coupe" 
car.color = "red"
car.brand = "Cadillac"
car.speed = "210kph"
print(car.type,car.color,car.brand,car.speed)
print(car.forward(400),'\n')

ok = automoblie()
ok.type = "pickup" 
ok.color = "orange"
ok.brand = "Toyota"
ok.speed = "60kph"
print(ok.type,ok.color,ok.brand,ok.speed)
print(ok.forward(200),'\n')
