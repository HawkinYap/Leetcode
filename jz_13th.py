# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a = []
        b = []
        for i in array:
            if i & 1:
                a.append(i)
            else:
                b.append(i)
        return a+b

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.reOrderArray(array))