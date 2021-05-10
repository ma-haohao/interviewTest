class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class BinaryTree:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def delete(node):
    nextN=node.next
    node.value=nextN.value
    node.next=nextN.next
    nextN.next=None

def mergeTwoLists(l1,l2):
    root=ListNode(None)
    cur=root
    while l1 and l2:
        if l1.val<l2.val:
            node=ListNode(l1.val)
            l1=l1.next
        else:
            node=ListNode(l2.val)
            l2=l2.next
        cur.next=node
        cur=node
    #l1或者l2可能还有剩余元素
    if l1 is None:
        cur.next=l2
    else:
        cur.next=l1
    return root.next

def levelOrder(self,root):
    res=[]
    cur_nodes=[root]
    nex_nodes=[]
    res.append([i.val for i in cur_nodes])
