class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        slist = s.split( )
        for i in slist:
            result.append(i[::-1])
        return(" ".join(result))

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution = Solution()
    print(solution.reverseWords(s))