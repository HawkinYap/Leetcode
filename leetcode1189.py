class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        res = 0
        while True:
            for letter in 'balloon':
                n = len(text)
                text = text.replace(letter,'',1)
                print(text)
                if len(text) == n:
                    return res
            else:
                res += 1

if __name__ == '__main__':
    text = "loonbalxballpoon"
    s = Solution()
    print(s.maxNumberOfBalloons(text))