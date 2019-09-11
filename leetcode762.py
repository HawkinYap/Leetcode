class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        one_list = [2, 3, 5, 7, 11, 13, 17, 19]
        for a in range(L, R + 1):
            if bin(a).count('1') in one_list:
                count += 1
        return(count)

if __name__ == '__main__':
    L = 6
    R = 10
    s = Solution()
    print(s.countPrimeSetBits(L, R))