#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    counter = [0] * k
    boughtarr = []
    c = sorted(c)

    for i in range(k):
            if(counter[i]==0):
                boughtarr.append(c.pop())
                counter[i]+=1
    while(len(c)>0):
        minindex=counter.index(min(counter))
        boughtarr[minindex]+=c.pop()*(counter[minindex]+1)
        counter[minindex]+=1

    return sum(boughtarr)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nk = input().split()
#
#     n = int(nk[0])
#
#     k = int(nk[1])
#
#     c = list(map(int, input().rstrip().split()))
#
#     minimumCost = getMinimumCost(k, c)
#
#     fptr.write(str(minimumCost) + '\n')
#
#     fptr.close()


print(getMinimumCost(3,[390225,426456,688267,800389,990107,439248,240638,15991,874479,568754,729927,980985,132244,488186,5037,721765,251885,28458,23710,281490,30935,897665,768945,337228,533277,959855,927447,941485,24242,684459,312855,716170,512600,608266,779912,950103,211756,665028,642996,262173,789020,932421,390745,433434,350262,463568,668809,305781,815771,550800
]))