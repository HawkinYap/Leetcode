class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # max = 0
        # index = 0
        # for i in A:
        #     if A.count(i) > max:
        #         max = A.count(i)
        #         index = i
        # return(index)
        for a in A:
            if A.count(a) == int(len(A)/2 ):
                return(a)

if __name__ == '__main__':
    A = [1, 2, 3, 3]
    s = Solution()
    print(s.repeatedNTimes(A))