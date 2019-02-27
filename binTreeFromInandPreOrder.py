# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  ###DO AGAIN WITH BETTER RUNTIME
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (preorder == [] and inorder == []):
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        if (preorder == inorder and len(preorder) == 1):
            return root

        root_idx = inorder.index(root_val)

        lefti = inorder[0:root_idx]
        righti = inorder[root_idx + 1:len(inorder)]

        leftp = preorder[1:1 + len(inorder[0:root_idx])]
        rightp = preorder[1 + len(inorder[0:root_idx]):len(preorder)]

        root.left = self.buildTree(leftp, lefti)
        root.right = self.buildTree(rightp, righti)

        return root