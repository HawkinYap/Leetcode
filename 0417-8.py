# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        # stack = [pRoot, '#']
        # while stack:
        #     cur = stack.pop(0)
        #     if cur != '#':
        #         print(cur.val, end='')
        #         if cur.left:
        #             stack.append(cur.left)
        #         if cur.right:
        #             stack.append(cur.right)
        #         stack.append('#')
        #     else:
        #         print()

        if not pRoot:
            return []
        current = [pRoot]
        next_layer = []
        result = []
        while current:
            for i in current:
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            result.append([i.val for i in current])
            current,next_layer = next_layer,[]
        return result


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
    print(s.Print(a))