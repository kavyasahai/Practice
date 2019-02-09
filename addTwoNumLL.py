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

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6


def makenum(self):
    num=""
    node = self
    while node != None:
        num+=str(node.val)
        node = node.next
    return num

def addTwoNumbers(l1, l2):
    num1=makenum(l1)[::-1]
    num2=makenum(l2)[::-1]

    res=str(int(num1)+int(num2))
    res=res[::-1]
    head=Node(res[0])
    curr = head
    for i in range(1,len(res)):
        curr.next=Node(res[i])
        curr=curr.next

    return head



print(addTwoNumbers(node1,node4))