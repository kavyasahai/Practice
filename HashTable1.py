#hash table to calculate number of characters in a given string

import string

chars=list(string.ascii_lowercase);

frequency=[0]*26

print(frequency)

def hashFunc(c):
    return chars.index(c)

str=input("Enter string")


for i in str:
    index=hashFunc(i)
    frequency[index]+=1


for i in range(26):
    print(chars[i])
    print(frequency[i])


