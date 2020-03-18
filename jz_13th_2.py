# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # p1 = 0
        # while p1 < len(array):
        #     while p1 < len(array) and array[p1] & 1:
        #         p1 += 1
        #     p2 = p1+1
        #     while p2 < len(array) and not array[p2] & 1:
        #         p2 += 1
        #     if p2 < len(array):
        #         array.insert(p1,array.pop(p2))
        #         p1 += 1
        #     else:
        #         break
        # return array

        return sorted(array, key=lambda d:d&1, reverse=True)



if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.reOrderArray(array))