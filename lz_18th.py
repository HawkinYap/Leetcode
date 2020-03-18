# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        if root:
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    d = TreeNode(4)
    e = TreeNode(5)
    b.left = d
    e.right = e

    f = TreeNode(6)
    c.left = f

    s = Solution()
    print(s.Mirror(a))