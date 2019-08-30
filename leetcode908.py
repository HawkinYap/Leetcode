class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return(max(max(A) - min(A) - 2 * K, 0))

if __name__ == '__main__':
    A = [0, 10]
    K = 2
    s = Solution()
    print(s.smallestRangeI(A, K))