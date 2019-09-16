import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # len = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     len += 1
        
        # l = len // 2 + 1
        # curr = head
        # while l > 1 :
        #     curr = curr.next
        #     l -= 1
        # return(curr)
        count = 0
        res = {}
        while head != None:
            count += 1
            res[count] = head
            head = head.next
        j = count // 2 + 1
        return(res[j].val)

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    lst2 = []
    for i in lst:
        lst2.append(ListNode(i))
    for j in range(len(lst2) - 1):
        lst2[j].next = lst2[j+1]
    
    s = Solution()
    print(s.middleNode(lst2[0]))


   
    
