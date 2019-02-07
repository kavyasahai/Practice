def firstUniqChar(s):
    chardict={}
    for i in s:
        if(i in chardict):
            chardict[i]+=1
        else:
            chardict[i]=1
    print(chardict)
    for i in chardict:
        if(chardict[i]==1):
            return s.index(i)

    return -1



print(firstUniqChar(['k','a','a','v','k']))