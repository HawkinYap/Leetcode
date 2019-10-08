class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(chips)):
            count = 0
            for j in range(len(chips)):
                if abs(chips[i] - chips[j]) & 1 == 1:
                    count += 1
            res.append(count)
        return(min(res))


        
if __name__ == '__main__':
    chips = [1, 2, 3]
    s = Solution()
    print(s.minCostToMoveChips(chips))