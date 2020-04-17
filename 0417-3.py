# -*- coding:utf-8 -*-
class Solution:
    # def __init__(self):
    #     self._dict = {}
    #     self.word = []
    
    # def dfs(self, matrix, i, j, path):
    #     print(matrix[i][j], path[0])
    #     if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])):
    #         return
    #     if (i, j) in self._dict:
    #         return
    #     if matrix[i][j] is not path[0]:
    #         return
    #     if not path:
    #         return
    #     self._dict[(i,j)] = 1
    #     self.word.append(path[0])

    #     self.dfs(matrix, i+1, j, path[1:])
    #     self.dfs(matrix, i-1, j, path[1:])
    #     self.dfs(matrix, i, j+1, path[1:])
    #     self.dfs(matrix, i, j-1, path[1:])
    
    # def hasPath(self, matrix, rows, cols, path):
    #     # write code here
    #     initlst = []
    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == path[0]:
    #                 initlst.append((i,j))
                    
    #     for i in initlst:
    #         self.word.append(path[0])
    #         self.dfs(matrix, i[0], i[1], path[1:])
    #         if "".join(self.word) == path:
    #             return True
    #     return False

    def dfs(self, matrix, i, j, rows, cols, flag, path, k):
        index = i * cols + j
        if not ( 0 <= i < rows and 0 <= j < cols):
            return False
        if matrix[index] != path[k]:
            return False
        if flag[index]:
            return False

        if (k == len(path) - 1):
            return True

        flag[index] = True

        if (self.dfs(matrix, i-1, j, rows, cols, flag, path, k+1) or 
        self.dfs(matrix, i+1, j, rows, cols, flag, path, k+1) or
        self.dfs(matrix, i, j+1, rows, cols, flag, path, k+1) or
        self.dfs(matrix, i, j-1, rows, cols, flag, path, k+1)):
            return True
        flag[index] = False
        return False
        

    
    def hasPath(self, matrix, rows, cols, path):
        flag = [False] * rows * cols
        for i in range(rows):
            for j in range(cols):
                if (self.dfs(matrix, i, j, rows, cols, flag, path, 0)):
                    return True
        return False



if __name__ == "__main__":
    matrix = ['a', 'b', 'c', 'e','s', 'f', 'c', 's','a', 'd', 'e', 'e']
    rows, cols = 3, 4
    path = "bcced"
    s = Solution()
    print(s.hasPath(matrix, rows, cols, path))