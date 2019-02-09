class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


    def traverse(self):
        node=self
        while node!=None:
            print(node.val)
            node=node.next

    def size(self):
        node=self
        count=0
        while node!=None:
            count+=1
            node=node.next
        return count


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

def removeNthFromEnd(head, n):
    size=Node.size(head)
    pos=size-n
    curr=head
    prev=None

    if(pos==0):
        head=head.next
        return
    else:
        for i in range(0,pos):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        curr.next=None
        return


removeNthFromEnd(node1,5)
Node.traverse(node1)