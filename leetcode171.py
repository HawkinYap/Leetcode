class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = len(s)
        for i in s:
            res  = res * 26 + ord(i) - 65 + 1
            l -= 1
        return(res)

        
if __name__ == '__main__':
    s = 'ZY'
    solution = Solution()
    print(solution.titleToNumber(s))