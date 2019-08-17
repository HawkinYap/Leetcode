# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.res = list()

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            l=1+self.maxDepth(root.left)
            r=1+self.maxDepth(root.right)
            return max(l,r)

if __name__ == '__main__':
    root1 = TreeNode(3)
    n1 = TreeNode(9)
    root1.left = n1
    n2 = TreeNode(20)
    root1.right = n2
    n2.left = TreeNode(15)
    n2.right = TreeNode(7)

    s = Solution()
    print(s.maxDepth(root1))
