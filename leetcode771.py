class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for item in J:
            res += S.count(item)
        return(res)

if __name__ == '__main__':
    J = 'aA'
    S = 'aAAbbbb'
    solution = Solution()
    print(solution.numJewelsInStones(J, S))