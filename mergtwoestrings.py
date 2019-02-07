#Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
#NOTE: Add the whole string if other string is empty.
#Input:
#The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two strings S1 and S2.
#Output:
#For each test case, in a new line, print the merged string.
#Constraints:
#1 <= T <= 100
#1 <= |S1|, |S2| <= 104
# Example:
# Input:
# 2
# Hello Bye
# abc def
#
# Output:
# HBeylelo
# adbecf


from collections import deque

def merge(str1, str2):
    s1 = deque(str1)
    s2 = deque(str2)
    finalstr = []
    if (len(s1) >= len(s2)):
        for i in range(0, len(s2)):
            finalstr.append(s1.popleft())
            finalstr.append(s2.popleft())
        if (len(s1) > 0):
            for s in s1:
                finalstr.append(s)
    elif (len(s1) < len(s2)):
        for i in range(0, len(s1)):
            finalstr.append(s1.popleft())
            finalstr.append(s2.popleft())
        if (len(s2) > 0):
            for s in s2:
                finalstr.append(s)

    return ''.join(finalstr)

n = input()
str1=[None]*int(n)
str2=[None]*int(n)
for i in range(0, int(n)):
    str1[i],str2[i] = input().split(' ')

for i in range(0, int(n)):
    print(merge(str1[i],str2[i]))