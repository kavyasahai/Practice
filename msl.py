# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists( l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l2.val<=l1.val):
            temp = l2.next
            l2.next = l1
            l2 = temp
        elif(l1.val<l2.val):
            temp=l1.next
            l1.next=l2
            l1=temp




                # lm.next=l1.next
                # print("L1: ",l1.val)
                # print("LM: ",lm.val)
                # l1 = l1.next
                # lm=lm.next




node1=ListNode("1")
node2=ListNode("2")
node3=ListNode("4")
node1.next=node2
node2.next=node3


node4=ListNode("1")
node5=ListNode("2")
node6=ListNode("3")
node4.next=node5
node5.next=node6

print(mergeTwoLists(node1,node4))