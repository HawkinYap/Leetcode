# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        tmp = 1
        if exponent < 0：
            ab_ex = -exponent
            print(ab_ex)
            while ab_ex:
                tmp *= base
                ab_ex -= 1
            return 1/tmp
        while exponent > 0:
            tmp *= base
            exponent -= 1
        return tmp
            

if __name__ == "__main__":
    base = 2
    exponent = -3
    s = Solution()
    print(s.Power(base, exponent))