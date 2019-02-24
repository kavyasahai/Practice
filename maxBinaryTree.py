# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if (len(nums) == 0):
            return None
        if (len(nums) == 1):
            return TreeNode(nums[0])

        maxi = nums.index(max(nums))
        root = TreeNode(nums[maxi])

        lefta = nums[0:maxi]
        righta = nums[maxi + 1:len(nums)]

        root.left = self.constructMaximumBinaryTree(lefta)
        root.right = self.constructMaximumBinaryTree(righta)

        return root

