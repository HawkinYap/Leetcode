# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def leafSimilar(self, root1, root2):
    #     """
    #     :type root1: TreeNode
    #     :type root2: TreeNode
    #     :rtype: bool
    #     """
    #     def dfs(node):
    #         if node:
    #             if not node.left and not node.right:
    #                 yield node.val
    #             yield from dfs(node.left)
    #             yield from dfs(node.right)

    #     return list(dfs(root1)) == list(dfs(root2))

    
    def func(self, root, tmp):
        if root:
            if None==root.left and None==root.right:
                tmp.append(root.val)
            else:
                tmp=self.func(root.left,tmp)
                tmp=self.func(root.right,tmp)
        return tmp

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        tmp1=[]
        tmp2=[]
        tmp1=self.func(root1,tmp1)
        tmp2=self.func(root2,tmp2)
        return tmp1==tmp2
