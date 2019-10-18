class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        con = A.split(" ") + B.split(" ")
        count = {}
        for i in con:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        res = [k for (k,v) in count.items() if v == 1]
        return(res)

        

if __name__ == "__main__":
    A = "this apple is sweet"
    B = "this apple is sour"
    s = Solution()
    print(s.uncommonFromSentences(A, B))