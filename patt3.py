rows = int(input('Enter the number of lines '))
for i in range(1, rows+1):
    for j in range(1, rows+1-i+1):
        print(' ', end='') 
    for j in range(1, i+1):
        print('*', end='')  
    print()
