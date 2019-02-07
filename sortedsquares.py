def sortedSquares(A):
    final_arr=[]
    for i in A:
        final_arr.append(i**2)


    return sorted(final_arr)

print(sortedSquares([-4,-1,0,3,10]))
