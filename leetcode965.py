# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return(True)
        if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
            return(False)
        return(self.isUnivalTree(root.left) and (self.isUnivalTree(root.right)))

if __name__ == "__main__":
    root1 = TreeNode(2)
    n1 = TreeNode(2)
    n2 = TreeNode(2)
    root1.left = n1
    root1.right = n2
    n1.left = TreeNode(5)
    n1.right = TreeNode(2)
    s = Solution()
    print(s.isUnivalTree(root1))