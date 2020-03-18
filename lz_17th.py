# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2 or not pRoot1:
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.isSubTree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubTree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSubTree(pRoot1.left, pRoot.left) and self.isSubTree(pRoot1.right, pRoot2.right)

