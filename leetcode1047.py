class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        for s in S:
            if len(ans)>0 and ans[-1] == s:
                ans.pop()
            else:
                ans.append(s)
        return "".join(ans)
        

if __name__ == '__main__':
    S = "abbaca"
    s = Solution()
    print(s.removeDuplicates(S))