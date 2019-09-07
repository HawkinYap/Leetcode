# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        # if number == 0:
        #     return(0)
        # if number == 1:
        #     return(1)
        # if number == 2:
        #     return(2)
        # return(self.rectCover(number - 2) + self.rectCover(number - 1))
        if number <= 0:
            return(0)
        a, b = 1, 2
        while number >= 2:
            a, b = b, a + b
            number -= 2
        return(a)



if __name__ == '__main__':
    number = 10
    s = Solution()
    print(s.rectCover(number))
