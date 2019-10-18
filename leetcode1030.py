class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = {}
        for i in range(R):
            for j in range(C):
                dis = abs(i - r0) + abs(j - c0)
                res[(i, j)] = dis
        res = sorted(res.items(), key=lambda res:res[1])
        
        end = []
        for i in res:
            end.append(list(i[0]))
        return(end)


if __name__ == "__main__":
    R, C, r0, c0 = 1, 2, 0, 0
    s = Solution()
    print(s.allCellsDistOrder(R, C, r0, c0))