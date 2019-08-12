# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, p=0):
        self.val = x
        self.next = p
    
class Singlelinklist(object):
    def __init__(self):
        self.head = None
    
    def initList(self, data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
    
    def isEmpty(self):
        if self.head.next == 0:
            print("Empty List")
            return(1)
        else:
            return(0)
    
    def getLength(self):
        if self.isEmpty():
            exit(0)
        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return(len)
    
    def traveList(self):
        if self.isEmpty():
            exit(0)
        p = self.head
        while p:
            print(p.val)
            p = p.next
    
    def insertElem(self, key, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            exit(0)
        p = self.head
        i = 0
        while i < index:
            pre= p
            p = p.next
            i += 1
        node = ListNode(key)
        pre.next = node
        node.next = p
    
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            exit(0)
        i = 0
        p = self.head
        while p.next:
            pre = p
            p = p.next
            i +=1
            if i==index:
                pre.next = p.next
                p = None
                return(1)
        pre.next = None
    
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next




        
if __name__ == '__main__':
    data = [4, 5, 1, 9]
    node = 5
    l = Singlelinklist()
    l.initList(data)
    # l.traveList()

    # l.insertElem(66, 3)
    # l.traveList()

    l.deleteElem(2)
    l.traveList()
