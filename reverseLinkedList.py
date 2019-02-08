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

def reverseList(head):
    prev = None
    current = head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

    return head


Node.traverse(reverseList(node1))

# 1->2->3->4