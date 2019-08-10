class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return (False)
 
        len = 1
        while int(x / len) >= 10:
            len = int(len * 10)
 
        while x > 0:
            l = int(x / len)
            r = int(x % 10)
 
            if l != r:
                return (False)
 
            else:
                x = int((x % len) / 10)
                len = int(len / 100)
 
        return (True)
if __name__ == '__main__':
    x = 12321
    solution = Solution()
    print(solution.isPalindrome(x))