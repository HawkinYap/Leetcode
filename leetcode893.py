class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = set()
        for sub in A:
            print(sub[::2], sub[1::2])
            sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(sub)
        return len(res)
        

if __name__ == '__main__':
    A = ["abc","acb","bac","bca","cab","cba"]
    s = Solution()
    print(s.numSpecialEquivGroups(A))