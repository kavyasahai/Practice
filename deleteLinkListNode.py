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

node1.next=node2
node2.next=node3


def deleteNode(node):
    temp=node.next
    node.val=temp.val
    node.next=temp.next

deleteNode(node1)
Node.traverse(node1)