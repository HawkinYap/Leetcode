class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return(str.lower())

if __name__ == '__main__':
    str = 'LOVELY'
    solution = Solution()
    print(solution.toLowerCase(str))