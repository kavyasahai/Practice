def cipher(S,i,j,ch):
    string=list(S)
    temp=string[i:j+1]
    new=[]
    if(ch=="L"):
        for t in temp:
            if(t=='a'):
                new.append('z')
            elif (t=='A'):
                new.append("Z")
            else:
                new.append(chr(ord(t)-1))
    else:
        for t in temp:
            if (t == "z"):
                new.append("a")
            elif (t == "Z"):
                new.append("A")
            else:
                new.append(chr(ord(t)+1))
    ind = 0
    for idx in range(i,j+1):
        string[idx]=new[ind]
        ind+=1



    return "".join(string)



answer=cipher("abc",0,1,"L")
print(answer)
