class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        # res = []
        # lst = text.split(" ")
        # index = 0
        # while index <= len(lst) - 3:
        #     tmp = lst[index:index + 3]
        #     if tmp[0] == first and tmp[1] == second:
        #         res.append(tmp[2])
        #     index += 1
        # return(res)

        # re正则匹配解法
        import re
        # pattern = f'(?<={first}\s{second}\s)\w+'
        # return re.findall(pattern, text)
        # return re.findall(f'(?<={first}\W{second}\W)\w+', text)




if __name__ == "__main__":
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    s = Solution()
    print(s.findOcurrences(text, first, second))