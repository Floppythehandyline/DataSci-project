import numpy as n
count = 0
arr = n.array([1,2,3,4,5,6,7,8,9],dtype='str')
table = n.reshape(arr,[3,3])
def chec(inp):
    global count
    if count % 2 == 0:
        arr[inp] = "O"
    else:
        arr[inp] = "X"
    print(table)

def inp():
    global count
    while count<9:
        inp =( int(input('Enter :'))-1)
        chec(inp)
        count += 1

print("Enter number you want to change to X/O",'\n',table)
inp()