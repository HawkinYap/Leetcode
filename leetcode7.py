class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strx = str(x)
        if strx[0] == '-':
            strx = strx[len(strx)-1:0:-1]
            if int(strx) < 2 ** 31-1:
                return(-int(strx))
            else:
                return(0)
 
        else:
            strx = strx[::-1]
            if int(strx) < 2 ** 31-1:
                return(int(strx))
            else:
                return(0)

if __name__ == '__main__':
    num = 123
    solution = Solution()
    print(solution.reverse(num))