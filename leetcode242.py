class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return(sorted(t) == sorted(s))

        if len(s)!=len(t):
            return False
        else:
            dic = {}
            for i in s:
                if i in dic:
                    dic[i] +=1
                else:
                    dic[i] = 1
            for i in t:
                if i in dic:
                    dic[i] -= 1
                else:
                    return False
            for i in dic:
                if dic[i] != 0:
                    return False
        return True


if __name__ == "__main__":
    s, t = "aacc", "ccac"
    solution = Solution()
    print(solution.isAnagram(s, t))