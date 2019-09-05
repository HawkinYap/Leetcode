class Solution(object):
    def countNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        b = sorted(set(s))
        for i in b:
            d = s.count(i)
            if d != 1:
                c += 1
        return(len(set(s)) + c)
        
        
if __name__ == '__main__':
    s = ['a', 'a', 'b', 'b', 'e', 'e', 'e']
    solution = Solution()
    print(solution.countNumber(s))