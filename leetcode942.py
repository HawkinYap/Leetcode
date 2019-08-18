class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        h = 0
        e = len(S)
        res = []
        for i in S:
            if i == 'I':
                res.append(h)
                h += 1
            else:
                res.append(e)
                e -= 1
        res.append(h)
        return(res)

if __name__ == '__main__':
    S = "DDI"
    solution = Solution()
    print(solution.diStringMatch(S))