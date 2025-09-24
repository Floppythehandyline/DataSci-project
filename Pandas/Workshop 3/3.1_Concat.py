import pandas as p
sr1 = p.Series([5,7,10],index=list('abc'))
sr2 = p.Series([1,3,6],index=list('def'))

srA = p.concat([sr1,sr2],ignore_index=False)
srB = p.concat([sr1,sr2],ignore_index=True)
print(srA,2*'\n',srB)

#concat จะนำ series 2 ตัว มาต่อกัน


#----Exercise----
#มี array 2 ตัว คือ
#1) A เก็บค่าเฉพาะ 1-10
#2) B เก็บค่าเฉพาะ 11-20
#โดยจะให้ user ใส่ค่าเป็นเลขระหว่าง 1-20 จำนวน 10 รอบ และนำค่านั้นไป
#เก็บไว้ใน array 2 ตัว ตามเงื่อนไขที่โจทย์กำหนด จากนั้นแสดงผล A และ B 

A = p.Series([])
B = p.Series([])
for i in range(10):
    inp = int(input("Enter integer(1-20): "))
    if inp >= 1 and inp <= 20:
        if inp <= 10:
            temp = p.Series([inp])
            A = p.concat([A,temp],ignore_index=True)
        else:
            temp = p.Series([inp])
            B = p.concat([B,temp],ignore_index=True)
    else:
        print("-Invaild input-")
print()
print(A,2*'\n',B)