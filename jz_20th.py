# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []   
        self.minstack = []    
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minstack or node < self.minstack[-1]:
            self.minstack.append(node)
        
    def pop(self):
        # write code here
        if self.stack:
            a = self.stack.pop()
            if a == self.minstack[-1]:
                self.minstack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def min(self):
        # write code here
        if self.stack:
            return self.minstack[-1]
        else:
            return None
                
if __name__ == "__main__":
    s = Solution()
    s.push(3)
    s.push(1)
    s.push(2)
    s.push(1)
    s.pop()
    print(s.min())