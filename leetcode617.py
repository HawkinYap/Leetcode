# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.res = list()

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if(t1 == None and t2 == None):
            return None
        if(t2 == None):
            return t1
        elif(t1 == None):
            return t2
        else:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
            return t1

    def inorderTraversal(self, root: TreeNode):
        if root:
            self.t(root)
        return self.res

    def t(self, root):
        if root.left != None:
            self.t(root.left)
        self.res.append(root.val)
        if root.right != None:
            self.t(root.right)

if __name__ == '__main__':
    root1 = TreeNode(3)
    n1 = TreeNode(2)
    root1.left = n1
    n2 = TreeNode(4)
    root1.right = n2
    n1.left = TreeNode(0)
    n2.right = TreeNode(8)


    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(7)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    s = Solution()
    result =s.mergeTrees(root1,n1)
    print(result)
