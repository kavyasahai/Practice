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




def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    mid=Node.size(head)//2
    left=head
    curr=head
    count=0
    while curr is not None:
        if(count==mid):
            right=curr
        count+=1
        curr=curr.next

    sortList(left)
    sortList(right)

    i=0
    j=0
    k=0

    curr=head
    while i<Node.size(left) and j<Node.size(right):
        if(left.val<right.val):
            curr=left
            left=left.next
        else:
            curr=right
            right=right.next
        curr=curr.next

    while i<Node.size(left):
        curr=left
        curr=curr.next
        left=left.next

    while j<Node.size(right):
        curr=right
        curr=curr.next
        right=right.next
    #
    # return curr


Node.traverse(sortList(node1))



