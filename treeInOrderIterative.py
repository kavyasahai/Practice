# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ansarr = []
        stack = []
        curr = root

        while (curr is not None):
            if (curr.left is not None):
                stack.append(curr)
                curr = curr.left
                stack[-1].left = None
            else:
                ansarr.append(curr.val)
                if (curr.right is not None):
                    curr = curr.right
                else:
                    if len(stack) > 0:
                        item = stack.pop()
                        ansarr.append(item.val)
                        if (item.right) is not None:
                            curr = item.right
                        else:
                            if len(stack) > 0:
                                curr = stack.pop()
                            else:
                                break
                    else:
                        break

        if len(stack) > 0:
            while len(stack) != 0:
                ansarr.append(stack.pop())

        print(ansarr)

        return (ansarr)
