# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # lists = []
        # while listNode:
        #     lists.append(listNode.val)
        #     listNode = listNode.next
        # lists.reverse()
        # return(lists)
        if listNode is None:
            return([])
        else:
            return(self.printListFromTailToHead(listNode.next) + [listNode.val])



def CreateList(n):
    if n <= 0:
        return(False)
    if n == 1:
        return ListNode(1)
    else:
        listNode = ListNode(1)
        tmp = listNode
        for i in range(2, n+1):
            tmp.next = ListNode(i)
            tmp = tmp.next
    return(listNode)


if __name__ == '__main__':
    listNode = CreateList(15)
    s = Solution()
    print(s.printListFromTailToHead(listNode))
