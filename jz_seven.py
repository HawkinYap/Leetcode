# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        a, b= 1, 1
        for i in range(2, n):
            a, b = b, a+b
        
        return b

        

if __name__ == "__main__":
    n = 6
    s = Solution()
    print(s.Fibonacci(n))
