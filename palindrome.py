def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = []
        revnum = '';

        for digit in str(x):
            digits.append(digit)
        print(digits)

        for i in range(len(digits)):
            revnum += digits.pop()

        if str(revnum) == str(x):
            return True
        else:
            return False