# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
            
        a, b = 1, 2
        for i in range(2, number):
            a, b = b, a+b
        
        return b

if __name__ == "__main__":
    number = 5
    s = Solution()
    print(s.jumpFloor(number))