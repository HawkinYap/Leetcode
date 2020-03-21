class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        x0, xn, y0, yn = 0, len(matrix[0]), 0, len(matrix)
        left, bottom, right, top = False, False, True, False
        i, j = 0, 0
        size = xn * yn
        while len(res) < size:
            if right:
                res.append(matrix[i][j])
                j += 1
                if j >= xn:
                    right = False
                    bottom = True
                    j -= 1
                    i += 1
            elif bottom:
                res.append(matrix[i][j])
                i += 1
                if i >= yn:
                    bottom = False
                    left = True
                    i -= 1
                    j -= 1
                
            elif left:
                res.append(matrix[i][j])
                j -= 1
                if j < x0:
                    left = False
                    top = True
                    j += 1
                    i -= 1
                    y0 += 1
                    xn -= 1
                    yn -= 1
            else:
                res.append(matrix[i][j])
                i -= 1
                if i < y0:
                    top = False
                    right = True
                    i += 1
                    j += 1
                    x0 += 1
        return res

if __name__ == "__main__":
    matrix = [[1],[2], [3], [4]]
    s = Solution()
    print(s.printMatrix(matrix))