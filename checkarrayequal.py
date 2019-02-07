# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow.  Each test case contains 3 lines of input. The first line contains an integer N denoting the size of the array. The second line contains element of array A[]. The third line contains elements of the array B[].
#
# Output:
# For each test case, print 1 if the arrays are equal else print 0.
# Example:
# Input:
# 2
# 5
# 1 2 5 4 0
# 2 4 5 0 1
# 3
# 1 2 5
# 2 4 15
# Output:
# 1
# 0

def findequalarr(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    for a in arr1:
        if(a in arr2):
            n1-=1
            n2-=1
        else:
            return 0
    if(n1==0 and n2==0):
        return 1
    else:
        return 0



n = input()
arr=[]
resultarr=[]

for i in range(0, int(n)):
    num =input()
    intlist1=[x for x in input().split()]
    intlist2=[x for x in input().split()]
    resultarr.append(findequalarr(intlist1,intlist2))


for i in range(0, int(n)):
    print(resultarr[i])