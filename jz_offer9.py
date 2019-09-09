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
        return 0
        list = [1,2]
        while number>=2:
            list[0],list[1] = list[1], list[0]+list[1]
            number -= 1
        return list[0]




if __name__ == '__main__':
    number = 10
    s = Solution()
    print(s.rectCover(number))
