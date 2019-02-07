def isAnagram(s,t):

    strs = []
    strt = []
    for i in s:
        strs.append(i)
    for i in t:
        strt.append(i)

    print(strs)
    print(strt)

    if(len(strs)!=len(strt)):
        return False

    for i in strt:
        if (i in strs):
            strs.remove(i)

    if (len(strs) == 0):
        return True
    else:
        return False


print(isAnagram('ab','ab'))