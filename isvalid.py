from collections import deque

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        mystack=[]
        paranthesis={"(":")","[":"]","{":"}","}":"{","]":"[",")":"("}
        for char in s:
            if(len(mystack)>0):
                if char==paranthesis[mystack[len(mystack)-1]]:
                    mystack.pop()
                else:
                    mystack.append(char)
            else:
                mystack.append(char)

        if(mystack):
            return False
        else: return True


print(isValid("({})({)"))
