# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = list()

    def invertTree(self, root):
        if(root == None):
            return
        rightTree = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(rightTree)
        return root

    #中序遍历验证是否翻转正确
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
    root = TreeNode(3)
    n1 = TreeNode(2)
    root.left = n1
    n2 = TreeNode(4)
    root.right = n2
    n1.left = TreeNode(0)
    n2.right = TreeNode(8)

    s = Solution()
    Head =s.invertTree(root)
    result = s.inorderTraversal(Head)
    print(result)
