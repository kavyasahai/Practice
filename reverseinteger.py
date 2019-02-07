


def reverse(x):
        """
        :type x: int
        :rtype: int
        """

        digits = []
        revnum = '';

        for digit in str(x):
            digits.append(digit)
        print(digits)

        if('-' in digits):
            revnum+=digits.pop(0);
            print(digits)

        if (len(digits) == 1):
            revnum+=digits[0]
            return int(revnum,10)
        else:
            while(digits[-1] == '0'):
                    digits.pop()

            for i in range(len(digits)):
                    revnum+=digits.pop()


            a=2**31
            b=a*(-1)
            c=a-1
            d=int(revnum,10)
            print(d)
            if (d >= b) & (d <= c):
                return d
            else:
                return 0

print(reverse(1534236469))
