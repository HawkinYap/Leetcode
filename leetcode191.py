class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return(bin(n).count('1'))


if __name__ == '__main__':
    n = 1111111111100000001
    s = Solution()
    print(s.hammingWeight(n))