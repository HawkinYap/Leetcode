# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        
        if pNode.right:
            cur = pNode.right
            while cur.left:
                cur = cur.left
            return cur
        
        if not pNode.right:
            while pNode.next:
                if pNode is pNode.next.left:
                    return pNode.next
                else:
                    pNode = pNode.next
        