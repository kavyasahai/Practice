import math
def isPalindrome(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '1', '0', '2', '3', '4', '5', '6', '7', '8', '9']
    pal=[]
    for i in s:
        if(i.lower() in alphabet):
            pal.append(i.lower())

    print(pal)

    result = True

    if (len(pal) == 2 ):
        if(pal[0]!=pal[1]):
             result=False
        # else:
        #     result=True
    else:
        str_len = len(pal)
        for i in range(0, int(str_len / 2)):  # you need to check only half of the string
            if pal[i] != pal[str_len - i - 1]:
                result = False
                break

    return result



print(isPalindrome("0P"))