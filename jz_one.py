class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if  not array:
            return False
        
        cols = len(array[0])
        rows = len(array)
        
        col = cols - 1
        row = 0
        
        while row < rows and col >= 0:
            cur = array[row][col]
            if cur == target:
                return True
            elif cur < target:
                row += 1
            else:
                col -= 1
            
        return False

if __name__ == "__main__":
    target = 1
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    solution = Solution()
    print(solution.Find(target, array))