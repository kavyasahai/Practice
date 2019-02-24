

    class Solution(object):
        def oddEvenJumps(self, A):
            """
            :type A: List[int]
            :rtype: int
            """

            goodIndexes = []

            for i in range(len(A)):
                isValid = True
                jumpCount = 0
                onIndex = i
                while (onIndex <= len(A) - 1 and isValid is True):
                    jumpCount += 1
                    if (jumpCount % 2 != 0):
                        j = onIndex + 1
                        minimum = None
                        minIndex = None
                        while (j < len(A)):
                            if A[onIndex] <= A[j]:
                                if minimum is None:
                                    minimum = A[j]
                                    minIndex = j
                                else:
                                    if (A[j] < minimum):
                                        minimum = A[j]
                                        minIndex = j
                            j += 1
                        if (minimum is None):
                            isValid = False
                        else:
                            onIndex = minIndex
                            print(onIndex)
                    elif (jumpCount % 2 == 0):
                        j = onIndex + 1
                        maximum = None
                        maxIndex = None
                        while (j < len(A)):
                            if A[onIndex] >= A[j]:
                                if maximum is None:
                                    maximum = A[j]
                                    maxIndex = j
                                else:
                                    if (A[j] > maximum):
                                        maximum = A[j]
                                        maxIndex = j
                            j += 1
                        if (maximum is None):
                            isValid = False
                        else:
                            onIndex = maxIndex
                if (onIndex >= len(A) - 1):
                    goodIndexes.append(i)

            return len(goodIndexes)