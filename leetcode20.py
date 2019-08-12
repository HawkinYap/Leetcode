class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = ['(', '[', '{']
        end = [')', ']', '}']
        pair = ['()', '[]', '{}']
        res = []
 
        for i in s:
            if i in start:
                res.append(i)
            if i in end:
                if len(res)==0:
                    return(False)
                else:
                    tmp = res.pop() + i
                    if tmp not in pair:
                        return(False)
        if len(res):
            return(False)
        return(True)

if __name__ == '__main__':
    s = '([)]'
    solution = Solution()
    print(solution.isValid(s))