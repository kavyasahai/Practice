class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxStrLen = 0
        begin = 0
        end = 0
        S = list(s)
        ans = []

        for i, char in enumerate(S):
            begin = i
            charset = [char]
            end = begin + 1
            while (end < len(S)):
                if (S[end] not in charset):
                    charset.append(S[end])
                else:
                    break
                end += 1
            if (len(charset) > maxStrLen):
                ans = charset[:]
                maxStrLen = len(charset)

        return (len(ans))


