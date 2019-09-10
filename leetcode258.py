class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            s = 0
            while num >= 1:
                s += num%10
                num /= 10
            num = s
        return(int(num))

if __name__ == "__main__":
    num = 258
    s = Solution()
    print(s.addDigits(num))
