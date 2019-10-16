class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return(not ('11' in str(bin(n)) or '00' in str(bin(n))))


if __name__ == "__main__":
    n = 5
    s = Solution()
    print(s.hasAlternatingBits(n))