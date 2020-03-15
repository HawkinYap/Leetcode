class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sindex = 0
        slen = 1

        matrix = [[False for _ in range(len(s))] for _ in range(len(s))]

        if len(s) == 1:
            return s

        for i in range(len(s)):
            matrix[i][i] = True

        for j in range(1, len(s)):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        matrix[i][j] = True
                    else:
                        matrix[i][j] = matrix[i+1][j-1]
                    if (j - i + 1) > slen:
                        sindex = i
                        slen = (j - i + 1)
                else:
                    matrix[i][j] = False
        
        return s[sindex:sindex + slen]

                
        





if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))
