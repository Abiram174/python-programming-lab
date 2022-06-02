b=int(input("enter your basic salary"))
if b<10000:
    h=.75*b
    d=.70*b
elif b>10000>=20000:
    h=.80*b
    d=.80*b
elif b>20000:
    h=.90*b
    d=.95*b
sal=b+h+d
print("salary is...",sal)
    
