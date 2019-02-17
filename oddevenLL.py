# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        else:
            curr = head
            curr2 = head.next
            count = 0

            while (curr.next is not None):
                nextinline = curr.next
                if (count % 2 == 0 and nextinline.next is None):
                    break
                curr.next = nextinline.next
                curr = nextinline
                count += 1

            curr.next = curr2

            return head