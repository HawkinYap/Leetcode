class Solution(object):
    def countNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return(i)
        
        
if __name__ == '__main__':
    s = "happyhacker"
    solution = Solution()
    print(solution.countNumber(s))