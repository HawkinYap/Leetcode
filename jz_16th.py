class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        cur = head = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                cur.next = pHead2
                pHead2 = pHead2.next
            else:
                cur.next = pHead1
                pHead1 = pHead1.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return head.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    e = ListNode(2)
    f = ListNode(5)
    e.next = f

    s = Solution()
    print(s.Merge(a, e))