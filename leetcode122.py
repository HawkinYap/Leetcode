class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices)-1, 0, -1):
            if prices[i] <= prices[i-1]:
                continue
            else:
                sum += prices[i] - prices[i-1]
 
        return(sum)

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))