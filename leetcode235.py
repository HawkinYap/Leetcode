# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if p.val < root.val > q.val:
        #     return(self.lowestCommonAncestor(root.left, p, q))

        # if p.val > root.val < q.val:
        #     return(self.lowestCommonAncestor(root.right, p, q))

        # return(root)

        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return(root)


if __name__ == '__main__':
    n1 = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(8)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(0)
    n5 = TreeNode(4)
    n2.left = n4
    n2.right = n5

    p, q = n2, n3
    s = Solution()
    print(s.lowestCommonAncestor(n1, p, q))