# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []
    def push(self, node):
        # write code here
        self.stackIn.append(node)
    def pop(self):
        # return xx
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop(-1))
        return(self.stackOut.pop(-1))

if __name__ == '__main__':
    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    solution.pop()
    solution.pop()
    

    
