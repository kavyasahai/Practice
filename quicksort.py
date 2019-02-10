def quicksort(arr):
    equal=[]
    less=[]
    greater=[]

    if(len(arr)>1):
        pivot=arr[0]
        for x in arr:
            if x<pivot:
                less.append(x)
            elif(x==pivot):
                equal.append(x)
            elif (x>pivot):
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr


print(quicksort([12,4,5,6,7,3,1,15]))