def spsquareprnt(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()
        
val = int(input("Enter the value:"))
square = spsquareprnt(val)
