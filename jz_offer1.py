# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # if not array:
        #     return(False)
        # else:
        #     if len(array) == 1 and not array[0]:
        #         return(False)
        #     if target < array[0][0] or target > array[-1][-1]:
        #         return(False)
        #     else:
        #         for i in array:
        #             if target in i:
        #                 return(True)

        row = 0
        col = len(array[0]) - 1
        if array == None:
            return False
        while row < len(array) and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -=1
            else:
                row +=1
        return False

            


if __name__ == '__main__':
    # array = [[2, 4, 5, 6], [7, 9, 10, 12], [13, 15, 16, 20]]
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    # array = [[]]
    target = 7
    s = Solution()
    print(s.Find(target, array))