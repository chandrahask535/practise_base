def mountain(n):
    for i in range(n):
        for j in range(i,n):
            print(' ', end=' ')
        for j in range(i+1):
            print('$', end=' ')
        for j in range(i):
            print('$', end=' ')
        print()
        
val = int(input("ENter the value:"))
triangle = mountain(val)
