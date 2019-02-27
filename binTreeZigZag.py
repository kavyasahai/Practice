# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        count = 1

        if root is None:
            return []

        queue = [root]
        mainqueue = []
        mainqueue.append(queue)
        ans = []

        while len(queue) > 0:
            temp = []
            queue = []
            if (count % 2 == 0):
                curr = mainqueue.pop(0)
                for c in range(len(curr) - 1, -1, -1):
                    temp += [curr[c].val]
                    if (curr[c].right is not None):
                        queue.append(curr[c].right)
                    if (curr[c].left is not None):
                        queue.append(curr[c].left)
            else:
                curr = mainqueue.pop(0)
                for c in range(len(curr) - 1, -1, -1):
                    temp += [curr[c].val]
                    if (curr[c].left is not None):
                        queue.append(curr[c].left)
                    if (curr[c].right is not None):
                        queue.append(curr[c].right)
            mainqueue.append(queue)
            ans.append(temp)
            count += 1

        return ans