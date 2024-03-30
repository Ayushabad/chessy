#...chessy...#
#Credits: Manogya Sharma
#Credits: Ayush Abad

import random

from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
a = int(input("Enter The Grid Size(2-10): "))
while a not in range(2,11):
    print("Wrong Input")
    a = int(input("Enter The Grid Size(2-10): "))
wall1 = wall2 = a + 1
print("Number of walls for each player is ",wall1)
irpos1=0
irpos2=2*(a-1)
icpos1=2*(random.randint(0,(a-1)))
icpos2=2*(random.randint(0,(a-1)))
cpos1=0
rpos1=0
cpos2=0
rpos2=0

path=[]
loc=[]

p1 = input("Enter Player 1 Name: ")
p2 = input("Enter Player 2 Name: ")

def ai(player,grid,size,pos):
    global cpos1,cpos2,rpos1,rpos2,p1,p2,wall1,wall2,path,loc
    left,right,up,down = None,None,None,None
    check = 0
    if player == 0:
        for i in range(rpos1+1,(2*size)-1,2):
            if grid[i][cpos1] == "=" or grid[i+1][cpos1] == "2":
                check = 0
                break
            else:
                check = 1
        if check == 0:
            if rpos1 < (2*size)-2:
                if grid[rpos1 +1][cpos1] != "=" and pos != 3 and grid[rpos1+2][cpos1] != "2":
                    down = grid[rpos1+2][cpos1]
                    rpos1=rpos1 + 2
                    cpos1=cpos1
                    loc.append(rpos1+1)
                    loc.append(cpos1+1)
                    path.append(loc)
                    if ai(player,grid,size,4):
                        return True
                else:
                    down = None
            else:
                down = None
            if cpos1 > 0:
                if grid[rpos1][cpos1 -1] != "||" and pos != 2 and grid[rpos1][cpos1-2] != "2":
                    left = grid[rpos1][cpos1 - 2]
                    rpos1=rpos1
                    cpos1=cpos1 - 2
                    loc.append(rpos1+1)
                    loc.append(cpos1+1)
                    path.append(loc)
                    if ai(player,grid,size,1):
                        return True
                    else:
                        pass
                else:
                    left = None
            else:
                left = None
            if cpos1 < (2*size)-2:
                if grid[rpos1][cpos1 +1] != "||" and pos != 1 and grid[rpos1][cpos1+2] != "2":
                    right = grid[rpos1][cpos1 + 2]
                    rpos1=rpos1
                    cpos1=cpos1 + 2
                    loc.append(rpos1+1)
                    loc.append(cpos1+1)
                    path.append(loc)
                    if ai(player,grid,size,2):
                        return True
                    else:
                        pass
                else:
                    right = None
            else:
                right = None
            if rpos1 > 0:
                if grid[rpos1-1][cpos1] != "=" and pos != 4 and grid[rpos1-2][cpos1] != "2":
                    up = grid[rpos1-2][cpos1]
                    rpos1=rpos1 - 2
                    cpos1=cpos1
                    loc.append(rpos1+1)
                    loc.append(cpos1+1)
                    path.append(loc)
                    if ai(player,grid,size,3):
                        return True
                else:
                    up = None
            else:
                up = None
            return False
        elif check == 1:
            rpos1=rpos1+2
            cpos1=cpos1
            loc.append(rpos1+1)
            loc.append(cpos1+1)
            path.append(loc)
            return True
    elif player == 1:
        for i in range(rpos2-1,0,-2):
            if grid[i][cpos2] == "=" or grid[i-1][cpos2] == "1":
                check = 0
                break
            else:
                check = 1
        if check == 0:
            if rpos2 > 0:
                if grid[rpos2-1][cpos2] != "=" and pos != 4 and grid[rpos2-2][cpos2] != "1":
                    up = grid[rpos2-2][cpos2]
                    rpos2=rpos2 - 2
                    cpos2=cpos2
                    loc.append(rpos2+1)
                    loc.append(cpos2+1)
                    path.append(loc)
                    if ai(player,grid,size,3):
                        return True
                else:
                    up = None
            else:
                up = None
            if cpos2 > 0:
                if grid[rpos2][cpos2 -1] != "||" and pos != 2 and grid[rpos2][cpos2-2] != "1":
                    left = grid[rpos2][cpos2 - 2]
                    rpos2=rpos2
                    cpos2=cpos2 - 2
                    loc.append(rpos2+1)
                    loc.append(cpos2+1)
                    path.append(loc)
                    if ai(player,grid,size,1):
                        return True
                    else:
                        pass
                else:
                    left = None
            else:
                left = None
            if cpos2 < (2*size)-2:
                if grid[rpos2][cpos2 +1] != "||" and pos != 1 and grid[rpos2][cpos2+2] != "1":
                    right = grid[rpos2][cpos2 + 2]
                    rpos2=rpos2
                    cpos2=cpos2 + 2
                    loc.append(rpos2+1)
                    loc.append(cpos2+1)
                    path.append(loc)
                    if ai(player,grid,size,2):
                        return True
                    else:
                        pass
                else:
                    right = None
            else:
                right = None
            if rpos2 < (2*size)-2:
                if grid[rpos2 +1][cpos2] != "=" and pos != 3 and grid[rpos2+2][cpos2] != "1":
                    down = grid[rpos2+1][cpos2]
                    rpos2=rpos2 + 2
                    cpos2=cpos2
                    loc.append(rpos2+1)
                    loc.append(cpos2+1)
                    path.append(loc)
                    if ai(player,grid,size,4):
                        return True
                else:
                    down = None
            else:
                down = None
            return False
        elif check == 1:
            rpos2=rpos2-2
            cpos2=cpos2
            loc.append(rpos2+1)
            loc.append(cpos2+1)
            path.append(loc)
            return True

def ifrow(grid, size):
    global icpos1,icpos2,irpos1,irpos2
    for i in range(irpos1,2*size):
            if grid[i][icpos1] == "=":
                break
            else:
                continue
    return True


def display(grid, size):
    print(6*" ",end="")
    for i in range(1,2*size):
        if i in range(10):
            print(i,end="     ")
        elif i in range(10,2*size):
            print(i,end="    ")

    print("")
    for r in range((2*size)-1):
        if r in range(9):
            print(r+1,end="   ")
        elif r in range(9,(2*size)-1):
            print(r+1,end="  ")
        for c in range((2*size)-1):
            if grid[r][c]=="0":
                print(" |__| ",end="")
            if grid[r][c]=="-" and (r%2!=0):
                print("------",end="")
            if grid[r][c]=="-" and (r%2==0):
                print("  |   ",end="")
            if grid[r][c]=="1":
                print(Fore.RED +" | 1| ",end="")
                print(Style.RESET_ALL,end="")
            if grid[r][c]=="2":
                print(Fore.GREEN + " | 2| ",end="")
                print(Style.RESET_ALL,end="")
            if grid[r][c]=="=" and (r%2!=0):
                print("======",end="")
            if grid[r][c]=="||" and (c%2!=0):
                print("  ||  ",end="")
        print("")
arr=[]
def dec(size):
    rows, cols = ((2*size-1),(2*size-1))
    for i in range(rows):
        col = []
        for j in range(cols):
            if (i%2)!=0:
                col.append("-")
            elif j%2==0:
                col.append("0")
            else:
                col.append("-")
        arr.append(col)
#    for r in range(rows):
#        print(arr[r])
def play(grid,size):
    grid[irpos1][icpos1]="1"
    grid[irpos2][icpos2]="2"
    print("")
    display(grid,size)

def ifwall(player):
    global wall1,wall2
    if player==0:
        if wall1>0:
            return True
        else:
            return False
    elif player==1:
        if wall2>0:
            return True
        else:
            return False

def movement(player,grid,size):
    global icpos1,icpos2,irpos1,irpos2,p1,p2,wall1,wall2
    a = input("Enter 1 to create wall or Enter 2 to move your goti: ")
    if a == "1":
        while True:
            if ifwall(player):
                z = input("if u want to enter wall horizontally or vertically (h/v): ")
                if z == "h" or z== "H":
                    wr = int(input("Enter Row Number: ")) - 1
                    wc = int(input("Enter Column Number: ")) - 1
                    if wr%2 != 0 and wr in range(2*size) and wc%2 == 0 and wc in range(2*size):
                        grid[wr][wc] = "="
                        if player==0:
                            wall1=wall1-1
                        elif player==1:
                            wall2=wall2-1
                        break
                    else:
                        print("This Row or Column Cannot Be Entered")
                        movement(x,grid,size)
                        break
                elif z == "v" or z== "V":
                    wr = int(input("Enter Row Number: ")) - 1
                    wc = int(input("Enter Column Number: ")) - 1
                    if wr%2 == 0 and wr in range(2*size) and wc%2 != 0 and wc in range(2*size):
                        grid[wr][wc] = "||"
                        if player==0:
                            wall1=wall1-1
                        elif player==1:
                            wall2=wall2-1
                        break
                    else:
                        print("This Row or Column Cannot Be Entered")
                        movement(x,grid,size)
                        break
                else:
                    print("Wrong input")
                    movement(x,grid,size)
                    break
            else:
                if player==0:
                    print("No more walls left for "+p1)
                elif player==1:
                    print("No more walls left for "+p2)
    elif a == "2":
        if player == 0:
            m = input("Enter Your Move In AWSD Form: ")
            if m == "A" or m == "a":
                if icpos1 > 0:
                    if grid[irpos1][icpos1 -1] != "||" and grid[irpos1][icpos1 -2] != "2":
                        grid[irpos1][icpos1] = "0"
                        icpos1 = icpos1 - 2
                        grid[irpos1][icpos1] = "1"
                    else:
                        print("This Move Cannot Be Made,Try Again")
                        print(p1 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This Move Cannot Be Made,Try Again")
                    print(p1 +"'s Turn")
                    movement(x,grid,size)
            elif m == "W" or m == "w":
                if irpos1 > 0:
                    if grid[irpos1-1][icpos1] != "=" and grid[irpos1-2][icpos1] != "2":
                        grid[irpos1][icpos1] = "0"
                        irpos1 = irpos1 - 2
                        grid[irpos1][icpos1] = "1"
                    else:
                        print("This Move Cannot Be Made,Try Again")
                        print(p1 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This Move Cannot Be Made,Try Again")
                    print(p1 +"'s Turn")
                    movement(x,grid,size)
            elif m == "S" or m == "s":
                print(irpos1)
                if irpos1 < (2*size)-1:
                    if grid[irpos1+1][icpos1] != "=" and grid[irpos1+2][icpos1] != "2":
                        grid[irpos1][icpos1] = "0"
                        irpos1 = irpos1 + 2
                        grid[irpos1][icpos1] = "1"
                    else:
                        print("This Move Cannot Be Made,Try Again")
                        print(p1 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This Move Cannot Be Made,Try Again")
                    print(p1 +"'s Turn")
                    movement(x,grid,size)
            elif m == "D" or m == "d":
                if icpos1 < (2*size)-1:
                    if grid[irpos1][icpos1+1] != "||" and grid[irpos1][icpos1 +2] != "2":
                        grid[irpos1][icpos1] = "0"
                        icpos1 = icpos1 + 2
                        grid[irpos1][icpos1] = "1"
                    else:
                        print("This Move Cannot Be Made,Try Again")
                        print(p1 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This Move Cannot Be Made,Try Again")
                    print(p1 +"'s Turn")
                    movement(x,grid,size)
            else:
                print("Your Input Is Wrong,Enter Again")
                print(p1 +"'s Turn")
                movement(player,grid,size)
        elif player == 1:
            m = input("Enter Your Move In AWSD Form: ")
            if m == "A" or m == "a":
                if icpos2 > 0:
                    if grid[irpos2][icpos2-1] != "||" and grid[irpos2][icpos2 -2] != "1":
                        grid[irpos2][icpos2] = "0"
                        icpos2 = icpos2 - 2
                        grid[irpos2][icpos2] = "2"
                    else:
                        print("This move cannot be made,Try Again")
                        print(p2 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This move cannot be made,Try Again")
                    print(p2 +"'s Turn")
                    movement(x,grid,size)
            elif m == "W" or m == "w":
                if irpos2 > 0:
                    if grid[irpos2-1][icpos2] != "=" and grid[irpos2-2][icpos2] != "1":
                        grid[irpos2][icpos2] = "0"
                        irpos2 = irpos2 - 2
                        grid[irpos2][icpos2] = "2"
                    else:
                        print("This move cannot be made,Try Again")
                        print(p2 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This move cannot be made,Try Again")
                    print(p2 +"'s Turn")
                    movement(x,grid,size)
            elif m == "S" or m == "s":
                if irpos2 < (2*size)-1:
                    if grid[irpos2+1][icpos2] != "=" and grid[irpos2+2][icpos2] != "1":
                        grid[irpos2][icpos2] = "0"
                        irpos2 = irpos2 + 2
                        grid[irpos2][icpos2] = "2"
                    else:
                        print("This move cannot be made,Try Again")
                        print(p2 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This move cannot be made,Try Again")
                    print(p2 +"'s Turn")
                    movement(x,grid,size)
            elif m == "D" or m == "d":
                if icpos2 < (2*size)-1:
                    if grid[irpos2][icpos2+1] != "||" and grid[irpos2][icpos2 + 2] != "1":
                        grid[irpos2][icpos2] = "0"
                        icpos2 = icpos2 + 2
                        grid[irpos2][icpos2] = "2"
                    else:
                        print("This move cannot be made,Try Again")
                        print(p2 +"'s Turn")
                        movement(x,grid,size)
                else:
                    print("This move cannot be made,Try Again")
                    print(p2 +"'s Turn")
                    movement(x,grid,size)
            else:
                print("Your Input Is Wrong,Enter Again")
                movement(player, grid, size)
    else:
        print("Wrong Input.")
        movement(player, grid, size)
def ifwin(player,size):
    global irpos1,irpos2
    if player==0:
        if irpos1==2*(size-1):
            return True
        else:
            return False
    elif player==1:
        if irpos2==0:
            return True
        else:
            return False
dec(a)
play(arr,a)

x = random.randrange(2)
if x==0:
    print(p1 + " gets to make his first move.")
elif x==1:
    print(p2 + " gets to make his first move.")

while True:
    if x == 0:
        print(p1 +"'s Turn")
        print(f"Number of walls left for {p1}: ",wall1)
        movement(x,arr,a)
        display(arr,a)
        rpos1=irpos1
        cpos1=icpos1
        if ai(x,arr,a,0):
            print(path[0])
            loc.clear()
            path.clear()
        else:
            print("ai does not work")
        if ifwin(x,a):
            print(p1 + " Wins.")
            break
        x = 1
    elif x == 1:
        print(p2 + "'s Turn")
        print(f"Number of walls left for {p2}: ",wall2)
        movement(x,arr,a)
        display(arr,a)
        rpos2 = irpos2
        cpos2 = icpos2
        if ai(x,arr,a,0):
            print(path[0])
            loc.clear()
            path.clear()
        else:
            print("ai does not work")
        if ifwin(x,a):
            print(p2 + " Wins.")
            break
        x = 0