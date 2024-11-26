def decreasing_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print('$', end=' ')
        print()
        
val = int(input("ENter the value:"))
left_triangle = decreasing_triangle(val)
        
