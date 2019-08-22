class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # a = []
        # b = []
        # for i in A:
        #     if i % 2 == 0:
        #         b.append(i)
        #     else:
        #         a.append(i)
        # a = sorted(a)
        # b = sorted(b)
        # return(b + a)
   
        A_len, i, j = len(A), 0, 1
        result = [0]*A_len
        for a in A:
            if a&1 == 0:
                result[i] = a
                i += 2
            else:
                result[j] = a
                j += 2
        return result


if __name__ == '__main__':
    A = [3,1,2,4]
    s = Solution()
    print(s.sortArrayByParity(A))