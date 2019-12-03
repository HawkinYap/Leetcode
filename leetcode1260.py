import copy
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # n = len(grid)
        # m = len(grid[0])
        # while k > 0:
        #     tmp = copy.deepcopy(grid)
        #     tmp[0][0] = grid[n-1][m-1]
        #     for i in range(len(grid)):
        #         for j in range(len(grid[i])):
        #             if j < m - 1:
        #                 tmp[i][j+1] = grid[i][j]
        #             if i < n - 1:
        #                 tmp[i+1][0] = grid[i][m-1]            
        #     grid = tmp
        #     k -= 1
        # return(grid)
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res.append(grid[i][j])
        idx = k % len(res)
        res[:] = res[len(res) - idx:] + res[:len(res) - idx]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = res.pop(0)
        return(grid)

if __name__ == "__main__":
    grid, k = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4
    s = Solution()
    print(s.shiftGrid(grid, k))
