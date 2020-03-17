# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        cur = listNode
        arr = []
        
        while cur:
            arr.append(cur.val)
            cur = cur.next
            
        return arr[::-1]

if __name__ == "__main__":

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    s = Solution()
    print(s.printListFromTailToHead(a))

