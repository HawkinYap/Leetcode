# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    # def __init__(self):
    #     self.lst = []
    def sortn(self, root, s):
        if not root:
            return s
        else:
            self.sortn(root.left, s)
            s.append(root)
            self.sortn(root.right, s)
        return s

    def KthNode(self, pRoot, k):
        # write code here
        # if not pRoot:
        #     return
        
        # self.lst.append(pRoot.val)
        # self.KthNode(pRoot.left, k)
        # self.KthNode(pRoot.right, k)

        
        # return sorted(self.lst)[k-1]
        s = []
        self.sortn(pRoot, s)
        if k == 0 or k > len(s):
            return False
        return s[k-1]

if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(7)
    a.left = b
    a.right = c

    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(8)

    b.left = d
    c.left = e
    c.right = f

    g = TreeNode(6)
    e.right = g

    k = 3

    s = Solution()
    print(s.KthNode(a, k))