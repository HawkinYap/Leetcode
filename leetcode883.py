class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 每一行最大值之和， 每一列最大值之和
        return(sum([sum(map(max, grid)), sum(map(max, zip(*grid))), sum(v > 0 for row in grid for v in row)]))
        

        
if __name__ == '__main__':
    grid = [[1,0],[0,2]]
    s = Solution()
    print(s.projectionArea(grid))