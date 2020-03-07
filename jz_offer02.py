# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        a = []
        for i in s:
            if i == ' ':
                a.append('%20')
            else:
                a.append(i)
        return ''.join(a)

        
if __name__ == "__main__":
    s = "We Are Happy"
    solution = Solution()
    print(solution.replaceSpace(s))