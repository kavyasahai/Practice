# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def constructArr(root):
    if (root is None):
        return []

    if (root.left is None and root.right is None):
        return [root.val]

    arr = constructArr(root.left) + [root.val] + constructArr(root.right)
    return arr


def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if (nums is None):
        return None
    if (len(nums) == 0):
        return None
    if (len(nums) == 1):
        return TreeNode(nums[0])

    maxi = nums.index(max(nums))
    root = TreeNode(nums[maxi])

    lefta = nums[0:maxi]
    righta = nums[maxi + 1:len(nums)]

    root.left = constructMaximumBinaryTree(lefta)
    root.right = constructMaximumBinaryTree(righta)

    return root


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        array = constructArr(root)
        array.append(val)
        print(array)

        return constructMaximumBinaryTree(array)