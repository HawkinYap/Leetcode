# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return(None)
        if len(pre) == 1:
            return(TreeNode(pre[0]))
        else:
            res = TreeNode(pre[0])
            res.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            res.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return(res)

    def postOrderTraverse(self, listnode):
        if listnode is None:
            return
        else:
            self.postOrderTraverse(listnode.left)
            self.postOrderTraverse(listnode.right)
            print(listnode.val)

                




if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    s = Solution()
    node = s.reConstructBinaryTree(pre, tin)
    print(s.postOrderTraverse(node))