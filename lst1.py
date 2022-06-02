
NumList = []
EvenSum = 0
OddSum = 0

n= int(input("Please enter the Total Number of List Elements: "))
for i in range(1, n +1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(n):
    if(NumList[j] % 2 == 0):
        EvenSum = EvenSum + NumList[j]
    else:
        OddSum = OddSum + NumList[j]

print("\nThe Sum of Even Numbers in this List =  ", EvenSum)
print("The Sum of Odd Numbers in this List =  ", OddSum)
