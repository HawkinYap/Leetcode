class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if not s and not p:
        #     return True
        
        # if s and not p:
        #     return False

        # if len(p) > 1 and p[1] == '*':
        #     if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #         return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        #     else:
        #         return self.isMatch(s, p[2:])           

        # if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #     if len(p) == 1:
        #         return self.isMatch(None, None)
        #     else:
        #         return self.isMatch(s[1:], p[1:])

        # else:
        #     return False

        a = [1,2,3]
        b = a[3:]
        if not b:
            print('o')



        
        



if __name__ == "__main__":
    s = 'a'
    p = '.'
    solution = Solution()
    print(solution.isMatch(s, p))