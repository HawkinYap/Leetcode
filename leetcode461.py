class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        n = bin(n)
        return(n.count('1'))

if __name__ == '__main__':
    x = 1
    y = 4
    solution = Solution()
    print(solution.hammingDistance(x, y))