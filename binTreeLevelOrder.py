# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None=

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if (root is None):
            return []

        queue = []
        queue.append(root)
        ans = []
        mainqueue = []
        mainqueue.append(queue)

        while len(queue) > 0:
            curr = mainqueue.pop(0)
            queue = []
            temp = []
            for c in curr:
                temp += [c.val]
                if (c.left is not None):
                    queue.append(c.left)
                if (c.right is not None):
                    queue.append(c.right)
            mainqueue.append(queue)
            ans.append(temp)

        return (ans)