class Solution(object):
    def longestPalindrome(self, s):

        size = len(s)

        if size < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(1, size - 1):
            palindrome_odd, odd_len = self.center_spread(s, size, i, i)
            palindrome_even, even_len = self.center_spread(s, size, i, i+1)

            cur_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_sub) > max_len:
                max_len = len(cur_sub)
                res = cur_sub

        return res


    def center_spread(self, s, size, left, right):
        i, j = left, right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1: j], j - (i + 1) 

if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))

