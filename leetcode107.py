# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

res = []
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return([])
        que = [root]
        res = []
        while que:
            tmp = []
            l = len(que)
            for i in range(l):
                t = que.pop(0)
                tmp.append(t.val)
                if t.left:
                    que.append(t.left)
                if t.right:
                    que.append(t.right)
            res.append(tmp)
        return(res[::-1])
        

if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n3.left = n4
    n3.right = n5

    s = Solution()
    print(s.levelOrderBottom(n1))