class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.a.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.b) == 0:
            while self.a:
                self.b.append(self.a.pop())
        return(self.b.pop())


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.b) == 0:
            while self.a:
                self.b.append(self.a.pop())
        return(self.b[-1])
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return(len(self.a) == 0 and len(self.b) == 0)
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(None)
obj.push(1)
obj.push(2)
obj.push(4)
param_2 = obj.pop()
print(param_2)
obj.push(5)
param_3 = obj.peek()
print(param_3)
obj.push(6)
param_4 = obj.empty()
print(param_4)