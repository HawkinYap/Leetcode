class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        _s = ''
        for i in s:
            if i == ' ':
                _s += '%20'
            else:
                _s += i
                
        return _s

if __name__ == "__main__":
    s = 'We%20Are%20Happy'
    solution = Solution()
    print(solution.replaceSpace(s))