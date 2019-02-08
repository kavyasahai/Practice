import math
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
node3=Node(1)
# node4=Node(1)
node1.next=node2
node2.next=node3
# node3.next=node4

def isPalindrome(head):
    stack=[]
    size=Node.size(head)
    curr=head
    result=True
    if(size%2==0):
        for i in range(math.floor(size/2)):
            stack.append(curr.val)
            curr=curr.next
    else:
        for i in range(math.ceil(size/2)):
            stack.append(curr.val)
            curr=curr.next
        stack.pop()
    head=curr
    while(curr is not None and len(stack)>0):
        if(curr.val==stack[-1]):
            stack.pop()
            curr=curr.next
        else:
            return False
            # curr = curr.next
    return result


print(isPalindrome(node1))



