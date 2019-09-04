class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # a = []
        # b = []
        # res = []
        # A = sorted(A)
        # for i in A:
        #     if i % 2 == 0:
        #         a.append(i)
        #     else:
        #         b.append(i)
        # for i in range(len(a)):
        #     res.append(a[i])
        #     res.append(b[i])
        # return(res)
        A = sorted(A)
        i, j = 0, 1
        res = [0] * len(A)
        for k in A:
            if k % 2 == 0:
                res[i] = k
                i += 2
            else:
                res[j] = k
                j += 2   
        return(res)     

if __name__ == '__main__':
    A = [4,2,5,7]
    s = Solution()
    print(s.sortArrayByParityII(A))