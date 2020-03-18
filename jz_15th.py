# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        p = pHead
        q = pHead.next
        while q:
            pHead.next = q.next
            q.next = p
            p = q
            q = pHead.next
        return p

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    s = Solution()
    print(s.ReverseList(a))