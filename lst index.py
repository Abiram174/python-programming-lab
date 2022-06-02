#enter elemt of lis than swap first and last element with each other
temp=0
x=list(map(int,input('enter value').split()))
x[0],x[-1]=x[-1],x[0]
print(x)


