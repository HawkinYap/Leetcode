# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        nextlayer = []
        result = []
        while stack:
            for i in stack:
                if i.left:
                    nextlayer.append(i.left)
                if i.right:
                    nextlayer.append(i.right)
            result.append([i.val for i in stack])
            stack, nextlayer = nextlayer, []
            
        return result