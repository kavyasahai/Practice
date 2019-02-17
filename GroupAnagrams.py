class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_chars = {}
        final_arr = []

        for string in strs:
            original = string
            sorted_list = sorted(list(string))
            sorted_string = ""
            for i in sorted_list:
                sorted_string += i

            if sorted_string in sorted_chars:
                sorted_chars[sorted_string].append(original)
            else:
                arr = []
                arr.append(original)
                sorted_chars[sorted_string] = arr

        for key in sorted_chars:
            final_arr.append(sorted_chars[key])

        print(final_arr)
        return final_arr