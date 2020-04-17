# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + '!' + self.Serialize(root.left) + '!' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        lst = s.split('!')
        return self.DeserializeTree(lst)

    def DeserializeTree(self, lst):
        if len(lst) <= 0:
            return None
        val = lst.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.DeserializeTree(lst)
            root.right = self.DeserializeTree(lst)
        return root

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


    s = Solution()
    print(s.Serialize(a))