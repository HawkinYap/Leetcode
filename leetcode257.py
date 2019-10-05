# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return([])
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + i)
        return(paths)  
                

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(5)
    n2.right = n4

    s = Solution()
    print(s.binaryTreePaths(n1))