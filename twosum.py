from typing import Any, Union


def twoSum(nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for num in nums:
        #     print(num)
        #     complement=4
        #     print(complement)
        #     if (complement in nums):
        #         print(nums.index(complement))
        #         if(nums.index(num) != nums.index(complement)):
        #             return [nums.index(num),nums.index(complement)]
        collected = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in collected:
                return [collected[diff], idx]
            collected[val] = idx











print(twoSum([3,3],6))











