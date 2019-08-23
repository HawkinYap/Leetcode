class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return(s[::-1])
        
if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    solution = Solution()
    print(solution.reverseString(s))