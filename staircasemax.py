# Given N number of square blocks. The height of each square block is 1. The task is to create a  staircase of max height using these blocks.
#
# Note: The first stair would require only one block, the second stair would require two blocks and so on.
#
# Input:
#
# The first line of the input contains T i.e number of test cases. Each line of the test case contains a number  N i.e number of blocks.
#
# Output:
#
# Each new line of the output contains only one single integer i.e Maximum height of staircase.
# Input:
#
# 3
# 10
# 12
# 16
#
# Output:
#
# 4
# 4
# 5
#
def maxstair(numblocks):
    numblocks=int(numblocks)
    for i in range(0,numblocks):
        if((numblocks-i)>=0):
            numblocks-=i
        else:
            return i-1




n = input()
arr=[]
resultarr=[]

for i in range(0, int(n)):
    num=input()
    resultarr.append(maxstair(num))


for i in range(0, int(n)):
    print(resultarr[i])