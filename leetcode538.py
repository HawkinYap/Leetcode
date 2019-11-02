# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rdl(self, root, preans = 0):
        if root is None:
            return preans #遍历到底，将累加和返回出去，方便上一级累加
        
        root.val += self.rdl(root.right, preans) # 每一层的节点将右子树的累加和加进来
        return self.rdl(root.left, root.val) #左子树最终的累加和就是这个子树的全部累加和
            
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.rdl(root) #累加和起始状态为0
        return root

if __name__ == "__main__":
    n1 = TreeNode(5)
    n2 = TreeNode(2)
    n3 = TreeNode(13)
    n1.left = n2
    n1.right = n3
    s = Solution()
    print(s.convertBST(n1))
