def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    collected = {}
    final = []
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in collected:
            final.append([collected[diff], idx])
        collected[val] = idx
    return final


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        collected = []
        doneidx = []
        if (len(nums) < 3):
            return collected
        for i in range(len(nums)):
            diff = target - nums[i]
            twopair = twoSum(nums, diff)

            if twopair is not None:
                for each in twopair:
                    pair = []
                    if (i not in each):
                        each.append(i)
                        if each is not None:
                            for e in each:
                                pair.append(nums[e])
                            if sorted(pair) not in collected:
                                collected.append(sorted(pair))

        return collected





