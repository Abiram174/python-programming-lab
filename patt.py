rows=int(input("enter the number of rows you want to print:"))
for i in range(1,rows+1):
    for j in range(rows+1-i):
        print("*",end='')
    print()
