class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class transerval:
    def preorderTranserval_N(self,root):
        stack=[root]
        res=[]
        while stack:
            current=stack.pop()
            if current:
                res.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
        return res

    def preorderTranserval(self,root):
        res=[]
        def recursionPart(root):
            if not root:
                return None
            res.append(root.val)
            recursionPart(root.left)
            recursionPart(root.right)
        recursionPart(root)
        return res

    def inorderTranserval(self,root):
        res=[]
        def recursionPart(root):
            if not root:
                return None
            recursionPart(root.left)
            res.append(root.val)
            recursionPart(root.right)
        recursionPart(root)
        return res

    def inorderTranserval_N(self,root):
        res=[]
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return res
            current=stack.pop()
            res.append(current.val)
            root=current.right
        return res

    def postorderTranserval(self,root):
        res=[]
        def recursionPart(root):
            if not root:
                return None
            recursionPart(root.left)
            recursionPart(root.right)
            res.append(root.val)
        recursionPart(root)
        return res

    def postorderTranserval_N(self,root):
        stack1=[root]
        stack2=[]
        res=[]
        while stack1:
            current=stack1.pop()
            if current:
                if not current.left and not current.right:
                    res.append(current.val)
                    continue
                stack1.append(current.right)
                stack1.append(current.left)
                stack2.append(current)
        while stack2:
            current=stack2.pop()
            res.append(current.val)
        return res

#构造测试用二叉树,前序+中序
def buildBinaryTree(preList,inList):
    if not preList:
        return None
    root=TreeNode(preList[0])
    #在中序队列中找到相关位置
    i=inList.index(root.val)
    root.left=buildBinaryTree(preList[1:i+1],inList[0:i])
    root.right=buildBinaryTree(preList[i+1:],inList[i+1:])
    return root

if __name__ == '__main__':
    preList=[3,9,20,15,7]
    inList=[9,3,15,20,7]
    Tree=buildBinaryTree(preList,inList)
    method=transerval()
    res2=method.postorderTranserval(Tree)
    res1=method.postorderTranserval_N(Tree)
    print(res1)
    print(res2)