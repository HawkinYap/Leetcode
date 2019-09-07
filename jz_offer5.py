# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return(0)
        else:
            return(min(rotateArray))

if __name__ == '__main__':
    rotateArray = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.minNumberInRotateArray(rotateArray))