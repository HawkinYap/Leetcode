class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        start, count = 0, 0
        result = []
        for i, each in enumerate(S):
            if each == '(':
                count += 1
            if each == ')':
                count -= 1
            if count == 0:
                result.append(S[start + 1: i])
                start = i + 1
        return(''.join(result))

if __name__ == '__main__':
    S = '(()())(())'
    solution = Solution()
    print(solution.removeOuterParentheses(S))

        

