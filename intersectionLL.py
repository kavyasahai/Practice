# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr = headA
        arr = []
        while curr is not None:
            arr.append(curr)
            curr = curr.next

        curr2 = headB
        while curr2 is not None:
            if (curr2 in arr):
                return curr2
            curr2 = curr2.next

        return None

