class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = sorted(heights)
        count = 0
        for i in range(len(res)):
            if res[i] != heights[i]:
                count += 1
        return(count)


if __name__ == '__main__':
    heights = [1,1,4,2,1,3]
    solution = Solution()
    print(solution.heightChecker(heights))