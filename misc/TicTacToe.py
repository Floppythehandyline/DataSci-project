import numpy as n
count = 0
arr = n.array([1,2,3,4,5,6,7,8,9],dtype='str')
table = n.reshape(arr,[3,3])
win = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{6,4,8}]
OSel = []
XSel = []

def place(inp):
    global count
    if count % 2 == 0:
        if arr[inp] != "X":
            arr[inp] = "O"
            OSel.append(inp)
        else:
            count -= 1
    if count % 2 == 1:
        if arr[inp] != "O":
            arr[inp] = "X"
            XSel.append(inp)
        else:
            count -= 1 
    print(table)

def check():
    Hold1 = set(OSel)
    Hold2 = set(XSel)
    if Hold1 in win:
        print("O has won the game")
        return True
    if Hold2 in win:
        print("X has won the game")
        return True

def inp():
    global count
    while count<9:
        if check() == True:
            break
        inp =( int(input('Enter :'))-1)
        place(inp)
        count += 1
        
        
print("Enter number you want to change to X/O",'\n',table)
inp()