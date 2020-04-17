# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     num1 = self.getNumber(l1)
    #     num2 = self.getNumber(l2)
    #     # print(num1, num2)

    #     num = num1 + num2
    #     lst = self.getLst(num)
    #     return self.getNewList(lst)


    # def getLst(self, num):
    #     lst = []
    #     if num == 0:
    #         lst.append(num)
    #         return lst
    #     while num:
    #         lst.append(num%10)
    #         num = num // 10
    #     return lst

    # def getNumber(self, l1):
    #     lst = []
    #     while l1:
    #         lst.append(l1.val)
    #         l1 = l1.next

    #     mul, result = 1, 0
    #     for i in lst:
    #         result += i * mul
    #         mul *= 10

    #     return result

    # def getNewList(self, num):
    #     head = ListNode(None)
    #     cur = head
    #     for i in num:     
    #         cur.next = ListNode(i)
    #         cur = cur.next
    #     # print(head.next.val)
    #     return head.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        res = head
        _ = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tmp = _ + x + y
            _ = tmp // 10
            # print(tmp)
            # print(_)
            # print(tmp%10)
            res.next = ListNode(tmp%10)
            res = res.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if _ > 0:
            res.next = ListNode(_)

        return head.next



if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    a.next = b
    b.next = c

    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    d.next = e
    e.next = f

    s = Solution()
    print(s.addTwoNumbers(a, d))

    
