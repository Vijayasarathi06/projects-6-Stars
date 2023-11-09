row=int(input("enter the value of row"))
for i in range(65,row+65):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()

row=int(input("enter the value of row"))
for i in range(65,row+65):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()
row=int(input("enter the value of row"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
row=int(input("enter the value of row"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
row=int(input("enter the value of row"))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
row=int(input("enter the value of row"))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
row=int(input("enter the value of row"))
for i in range(row):
    for j in range(i):
        print(" ",end="")
    for k in range(row-i):
        print("*",end=" ")
    print("")
row=int(input("enter the value of row"))
for i in range(row):
    for j in range(i):
        print("",end="")
    for k in range(row-i):
        print("*",end=" ")
    print("")
row=int(input("enter the value of row"))
for i in range(row):
    for j in range(i):
        print(" ",end=" ")
    for k in range(ro w-i):
        print("*",end=" ")
    print("")
row=int(input("enter the value of row"))
for i in range(row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print("")
               
