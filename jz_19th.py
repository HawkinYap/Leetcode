# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        
        if not matrix:
            return None
        
        while matrix:
            res += matrix.pop(0)
            if not matrix:
                return res
            matrix = self.transMatrix(matrix)
        return res
            
    def transMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        newmatrix = []
        for i in range(col - 1, -1, -1):
            tmp = []
            for j in range(row):
                tmp.append(matrix[j][i])
            newmatrix.append(tmp)
        # newmatrix.reverse()
        return newmatrix
        
            

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    s = Solution()
    print(s.printMatrix(matrix))