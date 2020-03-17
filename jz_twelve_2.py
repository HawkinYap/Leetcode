# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        flag = True
        if exponent < 0:
            exponent = -exponent
            flag = False

        # exponent & 1 == 1
        if exponent % 2 == 0:
            res = self.Power(base, exponent//2)
            res *= res
        else：
            res = self.Power(base, exponent//2)
            res *= res
            res *= base
        return res if flag else 1/res
            

if __name__ == "__main__":
    base = 2
    exponent = -3
    s = Solution()
    print(s.Power(base, exponent))