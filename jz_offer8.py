# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # num = [1, 1]
        # while len(num) <= number:
        #     num.append(2*num[-1])
        # return num[-1]

        a, b = 1, 1
        for _ in range(number):
            a, b = b, 2 * b
        return(a)

if __name__ == '__main__':
    number = 5
    s = Solution()
    print(s.jumpFloorII(number))
