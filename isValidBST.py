# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def returnChildren(root, arr):
    if (root.left is None and root.right is None):
        return root

    if (root.left):
        arr.append(root.left.val)
        returnChildren(root.left, arr)
    if (root.right):
        arr.append(root.right.val)
        returnChildren(root.right, arr)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isValid = True
        isValidLeft = True
        isValidRight = True

        if (root is None):
            return isValid

        if (root.left is not None):
            if (root.left.val >= root.val):
                isValid = False
            arrleft = []
            returnChildren(root.left, arrleft)
            for node in arrleft:
                if (node >= root.val):
                    isValid = False
            isValidLeft = isValid and self.isValidBST(root.left)

        if (root.right is not None):
            if (root.right.val <= root.val):
                isValid = False
            arrright = []
            returnChildren(root.right, arrright)
            for node in arrright:
                if (node <= root.val):
                    isValid = False
            isValidRight = isValid and self.isValidBST(root.right)

        return isValidLeft and isValidRight




