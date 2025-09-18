import pandas as p

da = {'sedan':2000,'suv':4000,'coupe':3500}
sr = p.Series(da)
print(sr)
#สร้างเครื่องคิดเลขแบบง่ายๆ ด้วย dictionary
print('\n','Basic calculator')
A = int(input("Enter A: "))
op = input("Enter operator(+ - * /): ")
B = int(input("Enter B: "))
ok = {'+':A+B, '-':A-B, '*':A*B, '/':A/B, '%':A%B, '//':A//B, '**':A**B}
print('Result: ',A,op,B," = ",ok[op])