# -*- coding:utf-8 -*-
class Solution:
    # def movingCount(self, threshold, rows, cols):
    #     # write code here
    #     sum = 0
    #     for i in range(rows):
    #         for j in range(cols):
    #             _s = self.sumNumber(i) + self.sumNumber(j)
    #             if _s <= threshold:
    #                 sum += 1
    #     return sum

    # def sumNumber(self, num):
    #     sum = 0
    #     while num:
    #         sum += num % 10
    #         num = num // 10

    #     return sum
    def __init__(self):
        self._dict = {}
        self.count = 0
    
    def get_sum(self, i, j):
        num = 0
        while i:
            num += i % 10
            i = i // 10
        
        while j:
            num += j % 10
            j = j // 10
        return num

    def dfs(self, matrix, k, i, j):
        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
            return
        if self.get_sum(i, j) > k:
            return
        if self._dict.get((i, j)):
            return
        self._dict[(i, j)] = 1
        self.count += 1

        self.dfs(matrix, k, i+1, j)
        self.dfs(matrix, k, i-1, j)
        self.dfs(matrix, k, i, j-1)
        self.dfs(matrix, k, i, j+1)

    def movingCount(self, threshold, rows, cols):
        x = [[1 for i in range(cols)] for j in range(rows)]
        self.dfs(x, threshold, 0, 0)
        return self.count



if __name__ == "__main__":
    rows, cols = 4, 4
    threshold = 3
    s = Solution()
    print(s.movingCount(threshold, rows, cols))