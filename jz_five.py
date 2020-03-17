# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        stack2 = []
        while self.stack1:
            stack2.append(self.stack1.pop())
        pop_node = stack2.pop()

        while stack2:
            self.stack1.append(stack2.pop())

        return pop_node

if __name__ == "__main__":
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.pop())
    print(s.pop())
