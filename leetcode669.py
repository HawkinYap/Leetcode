# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return(None)
            elif node.val > R:
                return(trim(node.left))
            elif node.val < L:
                return(trim(node.right))
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return(node)
        return(trim(root))


if __name__ == '__main__':
    L, R = 1, 3

    n1 = TreeNode(3)
    n2 = TreeNode(0)
    n3 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(2)
    n5 = TreeNode(1)
    n2.right = n4
    n4.left = n5
    s = Solution()
    print(s.trimBST(n1, L, R))