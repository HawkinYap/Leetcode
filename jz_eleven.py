# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # sum = 0
        # while n:
        #     tmp = n % 2
        #     if tmp == 1:
        #         sum += 1
        #     n = n // 2
        # return sum
        count = 0
        while n & 0xffffffff != 0:
            n = (n - 1) & n
            count += 1
        return count

if __name__ == "__main__":
    n = 5
    s = Solution()
    print(s.NumberOf1(n))