class Solution:
    def cutRope(self, number):
        # write code here
        # if number is 2:
        #     return 1
        
        # if number is 3:
        #     return 2
        
        # x = number // 3
        # y = number % 3
        
        # if y is 0:
        #     return pow(3, x)
        
        # elif y is 1:
        #     return 2 * 2 * pow(3, x-1)
        
        # else:
        #     return 2 * pow(3, x)

        if number is 0 or number is 1:
            return 0
        if number is 2:
            return 1
        if number is 3:
            return 2
        
        dp = [0, 1, 2, 3]
        for i in range(4, number + 1):
            _max = 0
            for j in range(1, i//2 + 1):
                tmp = dp[j] * dp[i - j]
                _max = _max if _max > tmp else tmp
            dp.append(_max)
        return dp[number]


if __name__ == "__main__":
    number = 9
    s = Solution()
    print(s.cutRope(number))
