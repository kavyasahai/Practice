class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

    def size(self):
        node = self
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count


node1 = Node(2)
node2 = Node(4)
node3 = Node(3)
node1.next=node2
node2.next=node3


def mergeThreeLists(l1, l2, l3):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1==None and l3==None:
        return l2
    elif l2==None and l3==None:
        return l1
    elif l1==None and l2==None:
        return l3

    if(l1.val<=l2.val and l1.val<=l3.val):
        head=l1
        head.next=mergeThreeLists(l1.next,l2,l3)
    elif(l2.val<=l1.val and l2.val<=l3.val):
        head=l2
        head.next=mergeThreeLists(l1,l2.next,l3)
    elif (l3.val <= l1.val and l3.val <= l2.val):
        head = l3
        head.next = mergeThreeLists(l1, l2, l3.next)

    return head


def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    curr=head
    equal=None
    less=None
    greater=None
    lesshead=None
    greaterhead=None
    equalhead=None
    if(Node.size(head)>1):
        pivot=head.val
        while(curr is not None):
            if(curr.val<pivot):
                if(less is None):
                    less=curr
                    lesshead=less
                else:
                    less.next=curr
                    less=less.next
                curr=curr.next
            elif(curr.val==pivot):
                if(equal is None):
                    equal=curr
                    equalhead=equal
                else:
                    equal.next=curr
                    equal=equal.next
                curr = curr.next
            elif (curr.val > pivot):
                if (greater is None):
                    greater = curr
                    greaterhead=greater
                else:
                    greater.next=curr
                    greater = greater.next
                curr = curr.next
        return mergeThreeLists(sortList(lesshead),equal,sortList(greaterhead))
    else:
        return head

Node.traverse(sortList(node1))



