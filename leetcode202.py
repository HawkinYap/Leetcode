class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """  
        t, T = 0, 50
        while t<T:
            ans = 0
            while n > 0:
                ans += (n%10) ** 2
                n = n // 10
            n = ans
            if n == 1:
                return(True)
            if n == 4:
                return(False)  # 4,16,37,58,89,145,42,20,4
        return(False)



if __name__ == "__main__":
    n = 19
    s = Solution()
    print(s.isHappy(n))