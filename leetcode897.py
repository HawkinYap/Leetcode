# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        s=[]
        dummy=TreeNode(0)
        p=dummy
        
        while s or root:
            if root:
                s.append(root)
                root=root.left
            else:
                cur=s.pop()
                root=cur.right
                cur.left=None
                p.right=cur
                p=p.right
        return dummy.right
        

if __name__ == '__main__':
    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(6)
    n1.left = n2
    n1.right = n3
    s = Solution()
    print(s.increasingBST(n1))