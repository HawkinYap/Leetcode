class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return([list(i) for i in (zip(*A))])

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.transpose(A))