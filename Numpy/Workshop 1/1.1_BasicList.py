listA = [1,2,3]
listB = [3,5,6]
the = []
#วนลูปบวกค่าที่อยู่ใน listA และ listB ที่ละ index
for i in range(len(listA)):
    the.append(listA[i] + listB[i]) 

print(the)