class Solution:
    def Find(self, target, array):
        # write code here
        # if array and len(array[0]) > 0:
        #     i = 0
        #     l = len(array[0]) - 1
        #     j = l
        #     current = array[0][j]
        #     while i <= l  and j >= 0:
        #         if current == target:
        #             return True
        #         elif target < current:
        #             current = array[i][j-1]
        #             j = j - 1
        #         else:
        #             if i == l:
        #                 return (False)
        #             else:
        #                 current = array[i+1][j]
        #                 i = i + 1
        #     return False
        # else:
        #     return False
        rows = len(array) - 1
        cols = len(array[0]) - 1
        if array and rows > 0 and cols > 0:
            i, j = 0, cols
            while i <= rows and j >= 0:
                print(array[i][j])
                if array[i][j] == target:
                    return True
                elif array[i][j] > target:
                    j = j - 1
                else:
                    i = i + 1
                
            return False
        return False
        

if __name__ == "__main__":
    array = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,10,15]]
    target = 1
    s = Solution()
    print(s.Find(target, array))