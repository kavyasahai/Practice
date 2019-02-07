class Solution(dict):
    answer=""
    def checkDictChildren(self,dict):
        pre = ""
        if(dict):
            for key,value in dict.items():
                if(len(value)>=2):
                    pre+=key
                    print(pre)
                    return pre
                else:
                    pre += key
                    print(pre)
                    pre+= self.checkDictChildren(value)
        return pre


    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        root = dict();
        _end=""

        for word in strs:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end]=_end
        print(root)
        if(len(root)>1):
            return ""
        else:
            sol= Solution({dict:root})
            return sol.checkDictChildren(root)




a=[""]
print(Solution.longestCommonPrefix(a))