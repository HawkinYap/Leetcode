# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return(a)

if __name__ == '__main__':
    n = 4
    s = Solution()
    print(s.Fibonacci(n))