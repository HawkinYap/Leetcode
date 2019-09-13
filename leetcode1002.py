class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        if not A:
            return(res)
        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)
            res += minnum*k
        return(res)
        

if __name__ == '__main__':
    A = ["bella","label","roller"]
    s = Solution()
    print(s.commonChars(A))