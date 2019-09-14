class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # candies2 = set(candies)
        # if len(candies2) <= len(candies) // 2:
        #     return(len(candies2))
        # else:
        #     return(len(candies) // 2)
        return(min(len(set(candies)), len(candies) // 2))
        
if __name__ == '__main__':
    candies = [1,1,2,3]
    s = Solution()
    print(s.distributeCandies(candies))