# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        newhead = RandomListNode(pHead.label)

        newhead.random = pHead.random
        newhead.next = self.Clone(pHead.next)
        return newhead


if __name__ == "__main__":

    a = RandomListNode(1)
    b = RandomListNode(2)
    c = RandomListNode(3)
    d = RandomListNode(4)

    a.next = b
    b.next = c
    c.next = d

    a.random = d
    b.random = c
    c.random = a

    s = Solution()
    print(s.Clone(a))