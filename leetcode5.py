class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_dict = {}
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    res_dict[s[i:j]] = (j-i)
                    break
        for k, v in res_dict.items():
            print(k, v)
        if not res_dict:
            return ""
        else:
            res = max(res_dict, key=lambda x: res_dict[x])
            return res




if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))
