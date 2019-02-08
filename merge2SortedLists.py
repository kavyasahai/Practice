class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


    def traverse(self):
        node=self
        while node!=None:
            print(node.val)
            node=node.next


node1=Node(1)
node2=Node(2)
node3=Node(5)
node1.next=node2
node2.next=node3

node4=Node(1)
node5=Node(4)
node6=Node(7)
node4.next=node5
node5.next=node6



def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1==None:
        return l2
    elif l2==None:
        return l1

    if(l1.val<=l2.val):
        head=l1
        head.next=mergeTwoLists(l1.next,l2)
    else:
        head=l2
        head.next=mergeTwoLists(l1,l2.next)

    return head


Node.traverse(mergeTwoLists(node1,node4))