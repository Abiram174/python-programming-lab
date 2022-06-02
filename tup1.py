#enter a tuple by user
#sum of elements within a tuple
s=0
x=tuple(map(int,input('enter value').split()))
for i in x:
    s=s+i
print(s)
