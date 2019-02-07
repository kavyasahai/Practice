# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        tempnode=head.next
        head.next=None
        tempnode.next=head


head=ListNode(1)
item2=ListNode(2)
head.next=item2

print(item1)
