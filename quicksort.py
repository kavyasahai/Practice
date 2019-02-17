def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

def quicksort(arr):
    # equal=[]
    # less=[]
    # greater=[]
    #
    # if(len(arr)>1):
    #     pivot=arr[0]
    #     for x in arr:
    #         if x<pivot:
    #             less.append(x)
    #         elif(x==pivot):
    #             equal.append(x)
    #         elif (x>pivot):
    #             greater.append(x)
    #     return quicksort(less) + equal + quicksort(greater)
    # else:
    #     return arr
    pivot=arr[len(arr)-1]
    for i in range(len(arr)):
        if()



print(quicksort([12,4,5,6,7,3,1,15]))