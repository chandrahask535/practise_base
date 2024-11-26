def increasing_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print('$', end=' ')
        print()
        
val = int(input("ENter the value:"))
left_triangle = increasing_triangle(val)
        
