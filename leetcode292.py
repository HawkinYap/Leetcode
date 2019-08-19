class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n%4==0 else True

if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.canWinNim(n))