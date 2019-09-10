class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index = -1000000
        ans = [0] * len(S)
        for i, s in enumerate(S):
            if s == C:
                index = i
            ans[i] = abs(i - index)
        index = -100000
        for i in range(len(S) - 1, -1 , -1):
            if S[i] == C:
                index = i
            ans[i] = min(abs(i - index), ans[i])
        return ans


if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    s = Solution()
    print(s.shortestToChar(S, C))