# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        res = [1, 2]
        for i in range(2,number):
            res.append(res[-1] * 2)
        return res[-1]


if __name__ == "__main__":
    number = 3
    s = Solution()
    print(s.jumpFloorII(number))