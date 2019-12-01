class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # num = 1
        # while num < N:
        #     num = (num << 1) + 1
        # return(N ^ num)

        return 2**(len(bin(N))-2)-1-N



if __name__ == "__main__":
    N = 5
    s = Solution()
    print(s.bitwiseComplement(N))