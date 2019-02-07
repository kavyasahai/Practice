import math

def reverseString(str):
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(math.ceil(len(str)/2)):
        temp=str[i]
        str[i]=str[len(str)-1-i]
        str[len(str)-1-i]=temp

    return str





print(reverseString(['h','e','l','l','o','o']))