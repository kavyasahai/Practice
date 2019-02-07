# Given an array of numbers, the task is to print only those numbers which have only 1, 2 and 3 as their digits.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an integer N and the second line contains N space separated array elements.
#
# Output:
# For each test case, In new line print the required elements in increasing order. if there is no such element present in the array print "-1".
# Example:
# Input:
# 2
# 3
# 4 6 7
# 4
# 1 2 3 4
#
# Output:
#
# -1
# 1 2 3
def linklist():

def rev(arr,num):







n = input()
arr=[]
resultarr=[]

for i in range(0, int(n)):
    num=input()
    arr = [x for x in input().split()]
    resultarr.append(rev(arr,num))


for i in range(0, int(n)):
    print(' '.join(resultarr[i]))