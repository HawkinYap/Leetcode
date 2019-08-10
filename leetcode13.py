class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = r_dict[s[0]]
        sum = 0
        if len(s) == 1:
            print(num)
        else:
            for i in s[1:]:
                if r_dict[i] <= num:
                    sum += num
                else:
                    sum -= num
                num = r_dict[i]
            sum += num
        return(sum)
if __name__ == "__main__":
    s = "III"
    solution = Solution()
    print(solution.romanToInt(s))