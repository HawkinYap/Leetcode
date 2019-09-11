# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head.next
        n = self.reverseList(p)

        head.next = None
        p.next = head
        return n

        # pre = None
        # cur = head

        # while cur != None:
        #     lat = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = lat

        # return pre

        

if __name__ == "__main__":

    h = ListNode(1)
    for i in range(1, 6):
        if i == 1:
            n1 = ListNode(i)
            h.next = n1
        else:
            n2 = ListNode(i)
            n1.next = n2
            n1 = n2

    s = Solution()
    print(s.reverseList(h))

    
        
            