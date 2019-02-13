# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hasharr = []
        curr = head
        while (curr is not None):
            if (curr.next in hasharr):
                return curr.next
            hasharr.append(curr)
            curr = curr.next

        return None