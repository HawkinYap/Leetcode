class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return(N % 2 == 0)

if __name__ == '__main__':
    N = 2
    s = Solution()
    print(s.divisorGame(N))