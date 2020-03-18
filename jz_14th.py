# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        _index = []
        cur = head
        while cur:
            _index.append(cur)
            cur = cur.next
        return _index[-k]

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    k = 3
    s = Solution()
    print(s.FindKthToTail(a, k))