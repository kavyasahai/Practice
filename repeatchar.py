# Given a string - "str", find the repeated character present first in the string.
#
# Example :
# Input  :  geeksforgeeks
# Output :  g
#           (mind that it will be g, not e.)
#
# Input :
# The first line of input contains an integer T denoting the Test cases. Then T test cases follow.
# Second line contains the string - "str"
#
# Output :
# repeated character present first in the string, if present
# otherwise print "-1"
#
#
# Input :
# 3
# hello
# fg
# geeksforgeeks
#
# Output :
# l
# -1
# g
#
def findrepchar(str):
    chararr=dict()
    for s in str:
        if(s in chararr):
            chararr[s]+=1
        else:
            chararr[s]=1
    for s in str:
        if(chararr[s]>1):
            return s
    return '-1'


n = input()
str=[]
for i in range(0, int(n)):
    str.append(input())

for i in range(0, int(n)):
    print(findrepchar(str[i]))
