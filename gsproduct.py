def prod(l,r,q):
    digres=[]
    count=0
    for i in range(l,r):
        dignum=[]
        for s in str(i):
            dignum.append(s)
        print(dignum)
        res=l*q
        for r in str(res):
            countin = 0;
            if(r in dignum):
                countin+=1
        if(countin==0):
            count+=1

    return count


print(prod(5,15,2))