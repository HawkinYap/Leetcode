class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # res = 0
        # for i in range(len(A[0])):
        #     tmp = []
        #     for j in range(len(A)):
        #         tmp.append(A[j][i])
        #     if sorted(tmp) != tmp:
        #         res += 1
        # return(res)

        res = 0
        for col in zip(*A):
            if sorted(col) != list(col):
                res += 1
        return(res)

if __name__ == '__main__':
    A = ["cba", "daf", "ghi"]
    s = Solution()
    print(s.minDeletionSize(A))