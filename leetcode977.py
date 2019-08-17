class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # res = []
        # for item in A:
        #     res.append(item ** 2)
        # return(sorted(res))
        return(sorted([item ** 2 for item in A]))

if __name__ == '__main__':
    A = [-4,-1,0,3,10]
    solution = Solution()
    print(solution.sortedSquares(A))