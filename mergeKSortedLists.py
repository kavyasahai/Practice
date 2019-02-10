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
node2=Node(4)
node3=Node(5)

node1.next=node2
node2.next=node3

node4=Node(1)
node5=Node(3)
node6=Node(4)
node4.next=node5
node5.next=node6

node7=Node(2)
node8=Node(6)
node7.next=node8

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


def mergeKLists(lists):
    if(len(lists)==0):
        return None
    elif(len(lists)==1):
        return lists[0]
    i=0
    temp=[]
    while(len(lists)!=1):
        if(i+1>=len(lists)):
            break
        newhead=mergeTwoLists(lists[i],lists[i+1])
        temp.append(newhead)
        i+=2
    if(len(lists)%2!=0):
        temp.append(lists[i])
    mergeKLists(temp)
    return newhead


ans=mergeKLists([node1,node4,node7])

Node.traverse(ans)

