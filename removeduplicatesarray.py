def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    for i in range(len(nums)-1,0,-1):
            if(nums[i]==nums[i-1]):
                nums.pop(i)
        # for i, vali in enumerate(nums):
        #     for j, valj in enumerate(nums):
        #         if (vali == valj and i != j):
        #             nums.pop(j)
        #             if (len(nums) == 2):
        #                 removeDuplicates(nums)




    return nums


ans=removeDuplicates([0,0,0,0,0])
print(ans)