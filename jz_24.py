# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.res = []
        if not root:
            return []
        
        self.subPath(root, [], expectNumber)
        # print(self.res)

        self.res = sorted(self.res, key=lambda x: len(x), reverse = True)
        return self.res

    def subPath(self, root, path, number):
        if not root.left and not root.right:
            if number == root.val:
                self.res.append(path+[root.val])

        if root.left:
            self.subPath(root.left, path+[root.val], number-root.val)
        if root.right:
            self.subPath(root.right, path+[root.val], number-root.val)


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    d = TreeNode(4)
    e = TreeNode(1)
    f = TreeNode(3)

    b.left = d
    b.right = e

    c.left = f

    g = TreeNode(3)
    e.left = g

    num = 7
    s = Solution()
    print(s.FindPath(a, num))