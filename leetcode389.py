from functools import reduce
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # return(chr(sum([ord(i) for i in t])-sum([ord(i) for i in s])))
        return(reduce(lambda x,y: chr(ord(x) ^ ord(y)),s+t))


if __name__ == "__main__":
    s = "ijksty"
    t = "ytskjie"
    ss = Solution()
    print(ss.findTheDifference(s, t))