def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    digits = [];
    for digit in s:
        digits.append(digit)
    l=len(digits)
    myDict={};
    myDict["I"]=1;
    myDict["V"] = 5;
    myDict["X"] = 10;
    myDict["L"] = 50;
    myDict["C"] = 100;
    myDict["D"] = 500;
    myDict["M"] = 1000;
    result=0;
    if (l == 0):
        return
    elif (l == 1):
        return myDict[digits.pop()]
    else:
        pass
    if(digits):
        d=digits.pop()
        if(d=="V" or d=="X")and (digits[-1]=="I"):
            a=myDict[d]-1
            digits.pop()
            if (digits):
                result+=a+self.romanToInt(digits)
                return result
            else:
                result+=a
                return result
        elif (d == "L" or d == "C") and (digits[-1] == "X"):
            a = myDict[d] - 10
            digits.pop()
            if (digits):
                result += a + self.romanToInt(digits)
                return result
            else:
                result+=a
                return result
        elif (d == "D" or d == "M") and (digits[-1] == "C"):
            a = myDict[d] - 100
            digits.pop()
            if (digits):
                result += a + self.romanToInt(digits)
                return result
            else:
                result+=a
                return result
        else:
            result+=myDict[d]+self.romanToInt(digits)
            return result

print(romanToInt("XC"))