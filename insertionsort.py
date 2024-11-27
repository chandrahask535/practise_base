def insertionsort(arr1):
    n =len(arr1)
    
    for i in range(1,n):
        key = arr1[i]
        j = i-1
        while j >= 0 and key < arr1[j]:
            arr1[j+1] = arr1[j]
            j-=1
        arr1[j+1] = key

arr1 = [50,30,20,10,40]
insertionsort(arr1)
print("sorted array", arr1)
        
            
    
